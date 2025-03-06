text_data = {
    "profitability": {
        "data": {
            "periods": ["2023-01", "2023-02", "2023-03", "2023-04", "2023-05", "2023-06", "2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12"],
            "operating_profit_margin": [-5, -10, 3, 4, -7, -8, 2, 0, -5, -15, -10, -12],
            "net_profit_margin": [-10, -15, 2, 3, -12, -13, 1, -1, -10, -18, -15, -17]
        },
        "description": {
            "operating_profit_margin": (
                "영업이익률: 전체적으로 영업이익률은 2023년 초반에는 마이너스에서 출발했으나, "
                "일부 달에서는 소폭의 양호한 실적을 보였습니다. 하지만 연말로 갈수록 다시 하락세를 "
                "보여 지속적인 개선이 필요합니다."
            ),
            "net_profit_margin": (
                "순이익률: 순이익률은 전반적으로 낮은 상태를 유지하고 있으며, 특히 연말로 갈수록 "
                "부정적인 수치를 기록하고 있습니다. 회사의 순이익을 증대시키기 위한 대책이 필요합니다."
            )
        }
    },
    "solvency": {
        "data": {
            "debt_to_equity_ratio": [55, 60, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56],
            "current_ratio": [180, 175, 170, 168, 166, 165, 160, 158, 157, 155, 152, 150]
        },
        "description": {
            "debt_to_equity_ratio": (
                "부채비율: 부채비율은 연중 안정적인 수준을 유지하고 있으며, 60%대에서 점차 감소하는 "
                "추세를 보이고 있습니다."
            ),
            "current_ratio": (
                "유동비율: 유동비율은 안정적으로 150%에서 180% 사이를 유지하며, 회사의 단기 채무 상환 능력이 "
                "우수함을 나타냅니다."
            )
        }
    },
    "efficiency": {
        "data": {
            "asset_turnover": [0.5, 0.52, 0.53, 0.55, 0.57, 0.58, 0.6, 0.62, 0.63, 0.64, 0.65, 0.66],
            "roe": [-5, -6, 0, 1, -2, -3, 2, 1, -4, -5, -6, -7]
        },
        "description": {
            "asset_turnover": (
                "자산 회전율: 자산 회전율은 점차 증가하는 추세를 보이며, 자산이 매출을 창출하는 데 점차 "
                "효율적으로 사용되고 있음을 시사합니다."
            ),
            "roe": (
                "ROE (자본 대비 순이익률): ROE는 일부 기간 동안 양호한 실적을 보였으나, 연말로 갈수록 "
                "부정적인 수치를 보였습니다. 자본의 효과적인 활용을 위해 개선이 필요합니다."
            )
        }
    }
}