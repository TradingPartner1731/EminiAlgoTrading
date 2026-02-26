# ARCH-0001: System Architecture & Directory Structure

**Status:** Proposed

**Date:** 2026-02-26

**Scope:** Core System Design

## 1. High-Level System Design

The bot follows an **Event-Driven Architecture**. Instead of a linear script, the system sits in a "Wait State" until a market event (Tick, Bar Close, or Order Fill) triggers a specific reaction.

### Components:

1. **Market Data Ingest (The Listener):** Asynchronous stream from IBKR.
2. **Signal Engine (The Brain):** Evaluates Price Action logic (e.g., VWAP deviations, candle patterns).
3. **Risk Manager (The Filter):** Validates every signal against the $50k account constraints.
4. **Execution Handler (The Hands):** Manages API order placement and "Bracket" management (Stop Loss/Take Profit).

---

## 2. Directory Structure

To maintain **interpretability**, the repository is organized by "concerns." A peer should be able to find the risk logic without digging through API connection code.

```text
.
├── src/                        # Source code (The "Live" Bot)
│   ├── main.py                 # Entry point: Orchestrates all modules
│   ├── engine/                 # Core logic
│   │   ├── strategy.py         # Price Action signal definitions
│   │   └── risk.py             # Position sizing & Kill-switch logic
│   ├── gateway/                # Connectivity
│   │   ├── ibkr_client.py      # IB_Async wrappers
│   │   └── data_streamer.py    # Real-time bar/tick handlers
│   └── utils/                  # Helpers (Logging, Slack/Discord alerts)
│
├── research/                   # The "Lab" (Non-production)
│   ├── notebooks/              # Jupyter Notebooks for Price Action EDA
│   └── backtests/              # Historical performance reports
│
├── data/                       # Local Data Store (Git-ignored)
│   ├── raw/                    # Stored CSVs/JSONs from API
│   └── processed/              # Continuous, back-adjusted contracts
│
├── docs/                       # Living Labs Documentation
│   ├── architecture/           # System design (This folder)
│   ├── decisions/              # ADRs (Architecture Decision Records)
│   └── logs/                   # Trading journals & Post-mortems
│
├── tests/                      # Unit tests for Math & Logic
├── .env                        # API Keys & Sensitive Configs
├── requirements.txt            # Dependency list
└── README.md                   # Project landing page

```

---

## 3. Data Flow Pattern

1. **Ingress:** `data_streamer.py` receives a 5-second bar.
2. **Notification:** The `DataStreamer` emits an event to `strategy.py`.
3. **Evaluation:** `strategy.py` checks if a "Price Action" setup exists.
4. **Validation:** If a setup exists, it sends a `TradeRequest` to `risk.py`.
5. **Execution:** If `risk.py` approves (Size < Max Risk), `ibkr_client.py` sends the order to the exchange.

---

## 4. Design Principles

* **Separation of Concerns:** The Strategy module knows nothing about "Ports" or "IP Addresses"; the Gateway module knows nothing about "Moving Averages."
* **Fail-Safe by Default:** If the connection to the broker drops, the `risk.py` module must assume a "Safe State" (stop all new entries).
* **Testability:** All math in `risk.py` and `strategy.py` must be covered by Unit Tests in the `/tests` folder.
