# 📈 E-Mini Programmatic Trading Bot (Project: Alpha-Stream)

A modular, price-action focused algorithmic trading system designed for the **S&P 500 E-mini (ES)** and **Micro E-mini (MES)** futures markets. This project follows the **Living Labs** methodology—documenting the evolution of strategies through real-world experimentation, peer feedback, and iterative refinement.

## 🔬 Living Labs Philosophy

This repository is more than just code; it is a living record of a trading journey. Every decision, failed experiment, and successful backtest is documented to ensure **interpretability** and **transparency**.

* **Co-Creation:** Designed to be audited and improved by trading peers.
* **Real-World Testing:** Transitioning from backtesting to paper trading to live markets in structured phases.
* **Documentation-First:** Code logic must be readable; architectural shifts must be justified.

---

## 🏗 Repository Structure

We maintain a strict documentation hierarchy to separate "The What" from "The Why."

* 📂 `src/`: The core Python engine, API connectors, and execution logic.
* 📂 `backtests/`: Strategy performance reports, Sharpe ratios, and drawdown analysis.
* 📂 `docs/architecture/`: High-level system design, data flow diagrams, and tech stack choices.
* 📂 `docs/decisions/`: **The Decision Log.** Records of why we chose specific risk parameters, APIs, or price-action patterns (ADRs - Architecture Decision Records).
* 📂 `data/`: (Git-ignored) Local SQLite/ArcticDB storage for historical OHLC data.

---

## 🛠 The Tech Stack

* **Language:** Python 3.11+ (Typed for clarity).
* **Execution:** `ib_async` (Interactive Brokers API).
* **Data Science:** `Pandas` / `Polars` for time-series manipulation.
* **Backtesting:** `VectorBT` or `Backtrader` for event-driven simulation.
* **Environment:** Chicago-based VPS for low-latency CME execution.

---

## 🛡 Risk Management Framework

The system operates under a **Capital Preservation First** mandate:

1. **Initial Account:** $50,000.
2. **Risk per Trade:** 1.0% (Fixed Fractional Sizing).
3. **Position Sizing Formula:** 
$$N = \frac{\text{Equity} \times 0.01}{\text{Stop Loss Points} \times \text{Point Value}}$$


4. **Kill Switch:** Automated liquidation if daily drawdown exceeds 5%.

---

## 🚀 Getting Started

### 1. Prerequisites

* Interactive Brokers TWS or IB Gateway installed.
* Python 3.11+ environment.

### 2. Installation

```bash
git clone https://github.com/your-username/trading-bot.git
cd trading-bot
pip install -r requirements.txt

```

### 3. Running the Data Stream

To verify the real-time connection to the CME:

```bash
python src/streamer.py --contract MES --expiry 202603

```

---

## 🤝 Peer Review & Contribution

If you are a trading peer reviewing this project:

1. Check `docs/decisions/` to understand the current logic.
2. Open an **Issue** if you spot "overfitting" in backtest results.
3. Submit a **PR** for improvements to the price-action signal detection modules.

---

## ⚖️ Disclaimer

*Futures trading contains substantial risk and is not for every investor. An investor could potentially lose all or more than the initial investment. Risk capital is money that can be lost without jeopardizing ones’ financial security or life style. Only risk capital should be used for trading.*
