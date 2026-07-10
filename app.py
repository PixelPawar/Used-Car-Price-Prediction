from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import joblib
from babel.numbers import format_currency

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
from datetime import datetime

app = Flask(__name__)


# Load Trained Model
model = joblib.load("models/used_car_price_model.pkl")



# Home
@app.route("/")
def home():
    return render_template("index.html")



# Predict Price
@app.route("/predict", methods=["POST"])
def predict():

    brand = request.form["brand"]
    model_name = request.form["model"]
    vehicle_age = float(request.form["vehicle_age"])
    km_driven = float(request.form["km_driven"])
    seller_type = request.form["seller_type"]
    fuel_type = request.form["fuel_type"]
    transmission_type = request.form["transmission_type"]
    mileage = float(request.form["mileage"])
    engine = float(request.form["engine"])
    max_power = float(request.form["max_power"])
    seats = float(request.form["seats"])

    input_df = pd.DataFrame({
        "brand": [brand],
        "model": [model_name],
        "vehicle_age": [vehicle_age],
        "km_driven": [km_driven],
        "seller_type": [seller_type],
        "fuel_type": [fuel_type],
        "transmission_type": [transmission_type],
        "mileage": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats]
    })

    prediction = model.predict(input_df)[0]

    formatted_price = format_currency(
        prediction,
        "INR",
        locale="en_IN"
    )

    return jsonify({
        "prediction": formatted_price,
        "brand": brand,
        "model": model_name,
        "vehicle_age": int(vehicle_age),
        "km_driven": f"{int(km_driven):,}",
        "seller_type": seller_type,
        "fuel_type": fuel_type,
        "transmission_type": transmission_type,
        "mileage": mileage,
        "engine": engine,
        "max_power": max_power,
        "seats": int(seats)
    })



# Download PDF Report
@app.route("/download-report", methods=["POST"])
def download_report():

    data = request.get_json()

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER
    title_style.textColor = colors.darkgreen

    heading_style = styles["Heading2"]
    heading_style.textColor = colors.darkgreen

    price_style = styles["Title"]
    price_style.alignment = TA_CENTER
    price_style.textColor = colors.green

    story = []

    
    # Title
    story.append(
        Paragraph(
            "USED CAR VALUATION REPORT",
            title_style
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            f"<b>Prediction Date:</b> {datetime.now().strftime('%d %B %Y | %I:%M %p')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    
    # Price
    story.append(
        Paragraph(
            "Estimated Selling Price",
            heading_style
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            data["prediction"],
            price_style
        )
    )

    story.append(Spacer(1, 25))

    
    # Vehicle Details
    story.append(
        Paragraph(
            "Vehicle Details",
            heading_style
        )
    )

    story.append(Spacer(1, 10))

    table_data = [

        ["Brand", data["brand"]],

        ["Model", data["model"]],

        ["Vehicle Age", f"{data['vehicle_age']} Years"],

        ["KM Driven", f"{data['km_driven']} km"],

        ["Seller Type", data["seller_type"]],

        ["Fuel Type", data["fuel_type"]],

        ["Transmission", data["transmission_type"]],

        ["Mileage", f"{data['mileage']} km/l"],

        ["Engine", f"{data['engine']} cc"],

        ["Maximum Power", f"{data['max_power']} bhp"],

        ["Seats", str(data["seats"])]

    ]

    table = Table(
        table_data,
        colWidths=[170, 260]
    )

    table.setStyle(

        TableStyle([

            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#198754")),

            ("TEXTCOLOR", (0, 0), (0, -1), colors.white),

            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

            ("BACKGROUND", (1, 0), (1, -1), colors.whitesmoke),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

            ("TOPPADDING", (0, 0), (-1, -1), 8),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE")

        ])

    )

    story.append(table)

    story.append(Spacer(1, 25))

    
    # ML Model Details
    story.append(
        Paragraph(
            "Machine Learning Model",
            heading_style
        )
    )

    story.append(
        Paragraph(
            "<b>Algorithm:</b> Extra Trees Regressor",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<b>R² Score:</b> 0.94",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<b>Mean Absolute Error (MAE):</b> ± ₹96,823",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<b>Dataset Size:</b> 15,411 Used Cars",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 30))

    
    # Footer
    story.append(
        Paragraph(
            "<font color='grey'>"
            "Generated by <b>Used Car Price Prediction</b><br/>"
            "Developed by <b>Atharva Pawar</b>"
            "</font>",
            styles["Normal"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="Used_Car_Valuation_Report.pdf",
        mimetype="application/pdf"
    )



if __name__ == "__main__":
    app.run(debug=True)