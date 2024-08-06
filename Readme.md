### MDD Invest

# Description

MDD Invest is a project to calculate and draw the Maximum Drawdown of a given stock. The Maximum
Drawdown is the maximum loss from a peak to a trough of a portfolio, before a new peak is attained.
The Maximum Drawdown is a measure of downside risk over a specified time period. It can be used both
as a stand-alone measure or as an input into other metrics such as "Return over Maximum Drawdown"
and the Calmar Ratio.

The project is divided into two parts: the first part is the calculation of the Maximum Drawdown and
the second part is the drawing of the Maximum Drawdown.

# Installation

To install the project, you need to clone the repository and install the requirements. The project
uses the following libraries:

- pandas
- numpy
- matplotlib
- yfinance
- Jinja2

To install the requirements, you can use the following command:

```bash
git clone
make install
```

# Usage

First, Change the ticker in the `finance/__init__.py` file to the desired stock. Then, you can run
the
`make run` command to calculate the Maximum Drawdown and draw the Maximum Drawdown.

```bash
make run
```

