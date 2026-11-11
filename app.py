
from pathlib import Path
import pandas as pd
import streamlit as st

BASE = Path(__file__).resolve().parent
DAY19 = BASE / "outputs/day19"
DAY20 = BASE / "outputs/day20"

st.set_page_config(
    page_title="Federated Network Anomaly Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Federated Network Anomaly Detection")
st.caption(
    "Adaptive Privacy-Preserving Federated Graph Neural Network"
)

metrics_path = DAY20 / "three_model_metrics.csv"
predictions_path = DAY20 / "three_model_predictions.csv"
weights_path = DAY19 / "adaptive_client_weights.csv"

missing = [
    str(path)
    for path in [metrics_path, predictions_path, weights_path]
    if not path.exists()
]

if missing:
    st.error("Required project output files are missing:")
    for path in missing:
        st.write(path)
    st.info("Complete Days 19 and 20 before launching this dashboard.")
    st.stop()

metrics = pd.read_csv(metrics_path)
predictions = pd.read_csv(predictions_path)
weights = pd.read_csv(weights_path)

st.subheader("Project overview")

c1, c2, c3 = st.columns(3)
c1.metric("Models compared", len(metrics))
c2.metric("Federated clients", len(weights))
c3.metric("Held-out test edges", len(predictions))

st.divider()

st.subheader("1. Compare model performance")

metric_columns = [
    col for col in [
        "accuracy", "precision", "recall",
        "f1_score", "roc_auc", "pr_auc"
    ]
    if col in metrics.columns
]

st.dataframe(metrics, use_container_width=True)

if metric_columns:
    chart_data = metrics.set_index("model")[metric_columns]
    st.bar_chart(chart_data)

st.caption(
    "Scores measure detection performance on the project's held-out "
    "test edges. They do not prove generalization to unseen networks."
)

st.divider()

st.subheader("2. Adaptive federated client weights")

weight_columns = [
    col for col in [
        "client", "training_edges",
        "standard_weight", "update_norm", "adaptive_weight"
    ]
    if col in weights.columns
]

st.dataframe(weights[weight_columns], use_container_width=True)

if {"client", "standard_weight", "adaptive_weight"}.issubset(weights.columns):
    chart_weights = weights.set_index("client")[
        ["standard_weight", "adaptive_weight"]
    ]
    st.bar_chart(chart_weights)

st.caption(
    "Adaptive weights are based on a prototype heuristic. "
    "They are not a formal privacy guarantee."
)

st.divider()

st.subheader("3. Inspect a test-edge prediction")

st.write(
    "Enter an edge index from the held-out test set. "
    "The dashboard will show the saved predictions from all three models."
)

edge_id = st.number_input(
    "Test edge index",
    min_value=0,
    max_value=2**31 - 1,
    value=int(predictions.iloc[0]["edge_index"]),
    step=1
)

matched = predictions[
    predictions["edge_index"] == edge_id
]

if matched.empty:
    st.warning(
        "This edge is not in the saved held-out test predictions. "
        "Try an edge index from the test split."
    )
else:
    row = matched.iloc[0]
    actual = int(row["actual_label"])

    st.metric(
        "Actual label",
        "Attack" if actual == 1 else "Benign"
    )

    model_prefixes = [
        ("Standard FedAvg", "standard_fedavg"),
        ("Adaptive FedAvg", "adaptive_fedavg"),
        ("Private FedAvg", "private_fedavg")
    ]

    available = []
    for label, prefix in model_prefixes:
        pred_col = f"{prefix}_prediction"
        prob_col = f"{prefix}_attack_probability"

        if pred_col in predictions.columns and prob_col in predictions.columns:
            available.append((label, pred_col, prob_col))

    if available:
        result_rows = []
        probability_data = {}

        for label, pred_col, prob_col in available:
            predicted = int(row[pred_col])
            probability = float(row[prob_col])

            result_rows.append({
                "Model": label,
                "Prediction": "Attack" if predicted == 1 else "Benign",
                "Attack probability": round(probability, 4),
                "Correct": predicted == actual
            })
            probability_data[label] = probability

        st.dataframe(
            pd.DataFrame(result_rows),
            use_container_width=True
        )

        st.write("Attack probability by model")
        st.bar_chart(
            pd.DataFrame.from_dict(
                probability_data, orient="index",
                columns=["Attack probability"]
            )
        )

st.divider()
st.caption(
    "Academic prototype using CIC-IDS2017. "
    "The private model uses a prototype noise mechanism and is not "
    "certified as differentially private."
)
