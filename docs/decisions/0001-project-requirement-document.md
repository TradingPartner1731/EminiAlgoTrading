# Project Requirement Document: E-mini Programmatic Trading Bot

## 1. Project Overview

The objective is to build a robust, interpretable, and testable programmatic trading system for E-mini futures (ES/MES). The system will focus on price-action logic, utilizing high-quality historical data for backtesting and real-time event-driven streaming for execution.

* **Initial Capital:** $50,000.
* **Primary Instrument:** Micro E-mini S&P 500 (MES) for granularity.
* **Core Philosophy:** Risk-first approach with automated position sizing and testable edge.

---

## 2. Technology Stack

To ensure maintainability and professional-grade performance, the following stack is selected:

| Component | Technology | Rationale |
| --- | --- | --- |
| **Language** | Python 3.11+ | Industry standard; high readability and massive library support. |
| **Data Analysis** | Pandas / Polars | Efficient manipulation of time-series OHLC and tick data. |
| **Backtesting** | `pysystemtrade` or `Backtrader` | Support for futures-specific logic (rolls, margin, and back-adjustment). |
| **Execution API** | IBKR via `ib_async` | Institutional-grade access; reliable Python wrappers available. |
| **Database** | SQLite or ArcticDB | Local storage for historical ticks and trade logs. |
| **Infrastructure** | Cloud VPS (Chicago-based) | Low latency to CME servers and 24/7 uptime. |

---

## 3. Data Architecture & Streaming

Data integrity is the foundation of the system. The bot requires two distinct data pipelines:

### 3.1 Historical Data (Research)

* **Source:** AlgoSeek or Interactive Brokers historical API.
* **Structure:** Continuous contracts (back-adjusted) to account for quarterly rolls.
* **Granularity:** 1-minute OHLC for strategy research; Tick data for slippage modeling.

### 3.2 Real-time Streaming (Execution)

* **Mechanism:** Event-driven subscription (not polling).
* **Stream Type:** 5-second real-time bars or Tick-by-Tick "Tape" data.
* **Logic:** The system listens for "Bar Updates" and triggers the logic engine only when a new data point is confirmed.

---

## 4. System Logic & Execution Engine

While specific strategies remain modular, the core engine must support the following:

* **Signal Processing:** Conversion of raw price streams into price-action signals (e.g., Breakouts, Mean Reversion).
* **Order Manager:** Handles limit order placement, cancellations, and "chasing" logic to minimize slippage.
* **State Management:** Tracking open positions, filled orders, and pending stops locally to ensure consistency with the broker.

---

## 5. Risk Management & Position Sizing

The bot will enforce strict mathematical constraints to protect capital.

### 5.1 Fixed Fractional Position Sizing

Positions are sized dynamically based on current account equity:

* **Risk per Trade:** Default 1.0% of total equity.
* **Calculation:** `Contracts = (Equity * Risk%) / (Stop Loss Distance * Point Value)`.

### 5.2 System Safeguards

* **Hard Stop Loss:** Every trade must be submitted with an attached (bracket) stop-loss order.
* **Daily Drawdown Limit:** Global "Kill Switch" if the account loses >5% in a single session.
* **Connectivity Check:** Automated heartbeat monitor to flatten positions if the API connection is lost for more than 60 seconds.

---

## 6. Development Roadmap

### Phase 1: Environment & Connectivity

* Setup Python virtual environment and IBKR Gateway.
* Verify API connectivity and "Paper Trading" account access.

### Phase 2: Data Pipeline & Backtesting

* Build automated downloader for continuous futures contracts.
* Implement the backtesting framework with realistic commissions and slippage.

### Phase 3: Logic Implementation

* Code the price-action signal logic.
* Run "Out-of-Sample" tests to validate the strategy win rate and expectancy ($E > 0$).

### Phase 4: Live Simulation (Forward Testing)

* Deploy bot on a VPS in a paper-trading environment.
* Monitor for "Slippage Variance" (Backtest results vs. Paper results).

### Phase 5: Production Deployment

* Go live with 1 MES contract to verify execution under real market liquidity.
* Scale position sizing according to the $50k risk model.

---

**Next Steps for Peer Review:**

* Review the choice of `ib_async` vs. proprietary cloud APIs (e.g., Tradovate).
* Audit the "Back-Adjustment" logic for the continuous historical data stream.
* Confirm the Daily Drawdown thresholds.
