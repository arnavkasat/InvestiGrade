# Real Estate Investment Scoring Model

## Overview

This project implements a **real estate investment scoring model** that evaluates locations based on five key parameters. The model assigns a **score from 0 to 100** and categorizes properties into **investment ratings (A+ to D)**.

## Parameters & Normalization

Each parameter is **normalized on a scale of 0 to 100** to ensure comparability.

| **Parameter**                        | **Raw Value Example** | **Normalization Formula**                                      |
| ------------------------------------ | --------------------- | -------------------------------------------------------------- |
| **Property Price Growth (%)**        | 2% to 10%             | \(S = \frac{X - X_{min}}{X_{max} - X_{min}} \times 100\)       |
| **Rental Yield (%)**                 | 3% to 10%             | \(S = \frac{X - X_{min}}{X_{max} - X_{min}} \times 100\)       |
| **Crime Rate (Per 1,000 Residents)** | 2 to 15 crimes        | \(S = 100 - \frac{X - X_{min}}{X_{max} - X_{min}} \times 100\) |
| **Proximity to Transit (Meters)**    | 100m to 2000m         | \(S = 100 - \frac{X - X_{min}}{X_{max} - X_{min}} \times 100\) |
| **Population Growth (%)**            | 0.5% to 3%            | \(S = \frac{X - X_{min}}{X_{max} - X_{min}} \times 100\)       |

## Weighted Scoring Formula

Each parameter contributes differently to the **final investment score**:

| **Parameter**             | **Weight (%)** |
| ------------------------- | -------------- |
| **Property Price Growth** | 30%            |
| **Rental Yield**          | 25%            |
| **Crime Rate**            | 20%            |
| **Proximity to Transit**  | 15%            |
| **Population Growth**     | 10%            |

The **final investment score** is computed as:

$$
Final Score = (S_{price} \times 0.3) + (S_{yield} \times 0.25) + (S_{crime} \times 0.2) + (S_{transit} \times 0.15) + (S_{population} \times 0.1)
$$

## Converting Score to Investment Rating

| **Final Score** | **Investment Rating**          | **Meaning**                   |
| --------------- | ------------------------------ | ----------------------------- |
| **85-100**      | **A+ (Prime Investment Zone)** | Excellent long-term potential |
| **70-84**       | **A (Good Investment Zone)**   | Strong investment potential   |
| **50-69**       | **B (Moderate Opportunity)**   | Moderate investment returns   |
| **30-49**       | **C (High Risk, Low Growth)**  | Limited investment potential  |
| **<30**         | **D (Poor Investment Zone)**   | High risk, weak returns       |
