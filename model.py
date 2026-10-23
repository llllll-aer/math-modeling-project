# -*- coding: utf-8 -*-
"""
项目名称：数模大赛求解程序（演示版）
功能模块：数据预处理 -> 算法求解 -> 结果可视化
作者：lei
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 模块1：数据预处理 (模拟读取和清洗赛题数据)
# ==========================================
def load_and_clean_data():
    print("[1/3] 正在加载并清洗数据...")
    # 模拟生成一组带有噪声的赛题数据 (例如：某地区历年经济指标)
    np.random.seed(42)
    X = np.linspace(0, 10, 50)
    # 真实趋势：y = 2x + 1，加入随机噪声
    y_true = 2 * X + 1
    y_noisy = y_true + np.random.normal(0, 2, 50)
    return X, y_noisy


# ==========================================
# 模块2：算法求解 (模拟将数学模型转化为代码)
# ==========================================
def solve_model(X, y):
    print("[2/3] 正在运行求解算法 (最小二乘法线性拟合)...")
    # 使用 NumPy 进行多项式拟合，模拟数模中的参数估计
    # 拟合一次多项式 (直线)，返回系数 [斜率, 截距]
    coefficients = np.polyfit(X, y, 1)
    slope, intercept = coefficients[0], coefficients[1]

    print(f"    -> 求解完成！模型拟合方程: y = {slope:.2f}x + {intercept:.2f}")
    return slope, intercept


# ==========================================
# 模块3：结果可视化 (模拟生成论文所需图表)
# ==========================================
def visualize_results(X, y, slope, intercept):
    print("[3/3] 正在生成可视化图表...")
    plt.figure(figsize=(8, 5))

    # 绘制原始带噪数据点
    plt.scatter(X, y, color='gray', label='Raw Data (Noisy)')

    # 绘制拟合出的模型曲线
    y_pred = slope * X + intercept
    plt.plot(X, y_pred, color='red', linewidth=2, label=f'Fitted Line: y={slope:.2f}x+{intercept:.2f}')

    plt.title('Math Modeling Demo: Data Fitting & Prediction')
    plt.xlabel('Input Variable (X)')
    plt.ylabel('Target Variable (Y)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # 保存图片到本地 (方便放进论文)
    plt.savefig('model_result.png')
    print("    -> 图表已生成并保存为 model_result.png")
    plt.show()


# ==========================================
# 主程序执行入口
# ==========================================
if __name__ == "__main__":
    print("=== 数学建模求解程序启动 ===")
    X_data, y_data = load_and_clean_data()
    slope, intercept = solve_model(X_data, y_data)
    visualize_results(X_data, y_data, slope, intercept)
    print("=== 程序运行结束，所有结果已交付 ===")