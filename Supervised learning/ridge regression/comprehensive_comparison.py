# COMPREHENSIVE MODEL COMPARISON
# Copy these cells into your ridge.ipynb notebook

# ============================================
# CELL 1: Import All Libraries
# ============================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

print("✅ All libraries imported successfully!")


# ============================================
# CELL 2: Load and Prepare Data
# ============================================
# Load data
data = load_diabetes()
X = data.data
y = data.target

# Train-test split (SAHI ORDER!)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

print(f"Training samples: {X_train.shape[0]}")
print(f"Test samples: {X_test.shape[0]}")
print(f"Features: {X_train.shape[1]}")


# ============================================
# CELL 3: Helper Function for Evaluation
# ============================================
def evaluate_model(model, X_train, X_test, y_train, y_test, model_name):
    """Train and evaluate a model"""
    # Train
    model.fit(X_train, y_train)
    
    # Predict
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Calculate metrics
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    test_rmse = np.sqrt(test_mse)
    test_mae = mean_absolute_error(y_test, y_test_pred)
    
    # Check overfitting
    overfitting = "Yes" if (train_r2 - test_r2) > 0.1 else "No"
    
    return {
        'Model': model_name,
        'Train R²': round(train_r2, 4),
        'Test R²': round(test_r2, 4),
        'RMSE': round(test_rmse, 2),
        'MAE': round(test_mae, 2),
        'Overfitting': overfitting
    }

print("✅ Helper function ready!")


# ============================================
# CELL 4: Test All Models
# ============================================
results = []

print("🚀 Starting model comparison...\n")

# 1. Linear Regression
print("1️⃣ Testing Linear Regression...")
lr = LinearRegression()
results.append(evaluate_model(lr, X_train, X_test, y_train, y_test, "Linear Regression"))

# 2. Ridge Regression (different alphas)
print("2️⃣ Testing Ridge Regression with different alphas...")
for alpha in [0.001, 0.01, 0.1, 1, 10, 100]:
    ridge = Ridge(alpha=alpha)
    results.append(evaluate_model(ridge, X_train, X_test, y_train, y_test, f"Ridge (α={alpha})"))

# 3. Lasso Regression
print("3️⃣ Testing Lasso Regression...")
lasso = Lasso(alpha=1.0, max_iter=10000)
results.append(evaluate_model(lasso, X_train, X_test, y_train, y_test, "Lasso (α=1.0)"))

# 4. ElasticNet
print("4️⃣ Testing ElasticNet...")
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5, max_iter=10000)
results.append(evaluate_model(elastic, X_train, X_test, y_train, y_test, "ElasticNet"))

# 5. Polynomial Regression (degree 2)
print("5️⃣ Testing Polynomial Regression (degree=2)...")
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
poly_lr = LinearRegression()
results.append(evaluate_model(poly_lr, X_train_poly, X_test_poly, y_train, y_test, "Polynomial (deg=2)"))

# 6. Polynomial + Ridge (degree 2)
print("6️⃣ Testing Polynomial + Ridge (degree=2, α=10)...")
poly_ridge = Ridge(alpha=10)
results.append(evaluate_model(poly_ridge, X_train_poly, X_test_poly, y_train, y_test, "Poly+Ridge (deg=2)"))

# 7. Decision Tree
print("7️⃣ Testing Decision Tree...")
dt = DecisionTreeRegressor(max_depth=5, random_state=42)
results.append(evaluate_model(dt, X_train, X_test, y_train, y_test, "Decision Tree (depth=5)"))

# 8. Random Forest
print("8️⃣ Testing Random Forest...")
rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
results.append(evaluate_model(rf, X_train, X_test, y_train, y_test, "Random Forest"))

# 9. Gradient Boosting
print("9️⃣ Testing Gradient Boosting...")
gb = GradientBoostingRegressor(n_estimators=100, max_depth=5, random_state=42)
results.append(evaluate_model(gb, X_train, X_test, y_train, y_test, "Gradient Boosting"))

# 10. SVR (Support Vector Regression)
print("🔟 Testing SVR...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
svr = SVR(kernel='rbf', C=10, gamma='scale')
results.append(evaluate_model(svr, X_train_scaled, X_test_scaled, y_train, y_test, "SVR (RBF kernel)"))

print("\n✅ All models tested!\n")


# ============================================
# CELL 5: Display Results in DataFrame
# ============================================
# Create DataFrame
df_results = pd.DataFrame(results)

# Sort by Test R² (descending)
df_results = df_results.sort_values('Test R²', ascending=False).reset_index(drop=True)

print("=" * 80)
print("📊 MODEL COMPARISON RESULTS (Sorted by Test R²)")
print("=" * 80)
print(df_results.to_string(index=False))
print("=" * 80)

# Find best model
best_model = df_results.iloc[0]
print(f"\n🏆 BEST MODEL: {best_model['Model']}")
print(f"   Test R² Score: {best_model['Test R²']}")
print(f"   RMSE: {best_model['RMSE']}")


# ============================================
# CELL 6: Visualize Results
# ============================================
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Test R² Score Comparison
ax1 = axes[0, 0]
colors = ['green' if x > 0.45 else 'orange' if x > 0.40 else 'red' for x in df_results['Test R²']]
ax1.barh(df_results['Model'], df_results['Test R²'], color=colors)
ax1.set_xlabel('Test R² Score', fontsize=12, fontweight='bold')
ax1.set_title('Test R² Score Comparison', fontsize=14, fontweight='bold')
ax1.axvline(x=0.44, color='red', linestyle='--', label='Baseline (0.44)')
ax1.legend()
ax1.grid(axis='x', alpha=0.3)

# 2. Train vs Test R² (Overfitting Check)
ax2 = axes[0, 1]
x_pos = np.arange(len(df_results))
width = 0.35
ax2.bar(x_pos - width/2, df_results['Train R²'], width, label='Train R²', alpha=0.8)
ax2.bar(x_pos + width/2, df_results['Test R²'], width, label='Test R²', alpha=0.8)
ax2.set_xlabel('Models', fontsize=12, fontweight='bold')
ax2.set_ylabel('R² Score', fontsize=12, fontweight='bold')
ax2.set_title('Train vs Test R² (Overfitting Check)', fontsize=14, fontweight='bold')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(df_results['Model'], rotation=45, ha='right', fontsize=8)
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# 3. RMSE Comparison
ax3 = axes[1, 0]
colors_rmse = ['green' if x < 55 else 'orange' if x < 60 else 'red' for x in df_results['RMSE']]
ax3.barh(df_results['Model'], df_results['RMSE'], color=colors_rmse)
ax3.set_xlabel('RMSE (Lower is Better)', fontsize=12, fontweight='bold')
ax3.set_title('RMSE Comparison', fontsize=14, fontweight='bold')
ax3.invert_xaxis()  # Lower RMSE on right
ax3.grid(axis='x', alpha=0.3)

# 4. Model Performance Summary
ax4 = axes[1, 1]
ax4.axis('off')
summary_text = f"""
MODEL PERFORMANCE SUMMARY
{'='*40}

🏆 Best Model: {best_model['Model']}
   • Test R²: {best_model['Test R²']}
   • RMSE: {best_model['RMSE']}
   • MAE: {best_model['MAE']}
   • Overfitting: {best_model['Overfitting']}

📈 Key Observations:
   • Total models tested: {len(df_results)}
   • Best Test R²: {df_results['Test R²'].max():.4f}
   • Worst Test R²: {df_results['Test R²'].min():.4f}
   • Average Test R²: {df_results['Test R²'].mean():.4f}

💡 Insights:
   • Ridge Regression helps when α is tuned
   • Ensemble methods (RF, GB) often perform better
   • Polynomial features can improve but risk overfitting
"""
ax4.text(0.1, 0.5, summary_text, fontsize=11, verticalalignment='center',
         family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Visualization saved as 'model_comparison.png'")


# ============================================
# CELL 7: Ridge Alpha Optimization
# ============================================
print("\n" + "="*80)
print("🔍 RIDGE REGRESSION: ALPHA OPTIMIZATION")
print("="*80)

alphas = [0.001, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000]
train_scores = []
test_scores = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    
    train_scores.append(ridge.score(X_train, y_train))
    test_scores.append(ridge.score(X_test, y_test))

# Find best alpha
best_alpha_idx = np.argmax(test_scores)
best_alpha = alphas[best_alpha_idx]
best_score = test_scores[best_alpha_idx]

print(f"\n🎯 Best Alpha: {best_alpha}")
print(f"   Test R² Score: {best_score:.4f}")

# Plot alpha vs R² score
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(alphas, train_scores, 'o-', label='Train R²', linewidth=2)
plt.plot(alphas, test_scores, 's-', label='Test R²', linewidth=2)
plt.axvline(x=best_alpha, color='red', linestyle='--', label=f'Best α={best_alpha}')
plt.xlabel('Alpha (log scale)', fontsize=12, fontweight='bold')
plt.ylabel('R² Score', fontsize=12, fontweight='bold')
plt.title('Ridge Regression: Alpha Tuning', fontsize=14, fontweight='bold')
plt.xscale('log')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.semilogx(alphas, train_scores, 'o-', label='Train R²', linewidth=2)
plt.semilogx(alphas, test_scores, 's-', label='Test R²', linewidth=2)
plt.axvline(x=best_alpha, color='red', linestyle='--', label=f'Best α={best_alpha}')
plt.fill_between(alphas, train_scores, test_scores, alpha=0.2, color='gray')
plt.xlabel('Alpha (log scale)', fontsize=12, fontweight='bold')
plt.ylabel('R² Score', fontsize=12, fontweight='bold')
plt.title('Train-Test Gap (Overfitting Check)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ridge_alpha_optimization.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Alpha optimization plot saved!")


# ============================================
# CELL 8: Final Recommendations
# ============================================
print("\n" + "="*80)
print("💡 RECOMMENDATIONS & INSIGHTS")
print("="*80)

recommendations = """
1️⃣ LINEAR VS RIDGE:
   • Linear Regression R² ≈ 0.44
   • Ridge Regression doesn't help much because:
     → Model is UNDERFITTING (not overfitting)
     → Need more complex features, not regularization
     → Ridge works when train >> test score

2️⃣ WHEN TO USE RIDGE:
   ✅ Use when: Train R² = 0.95, Test R² = 0.44 (overfitting!)
   ❌ Don't use when: Train R² = 0.44, Test R² = 0.44 (underfitting!)

3️⃣ BETTER ALTERNATIVES FOR THIS DATA:
   • Polynomial Features (degree 2-3)
   • Random Forest or Gradient Boosting
   • Feature Engineering (create interaction terms)
   • Try different feature combinations

4️⃣ KEY LEARNINGS:
   • More regularization (↑α) → Lower complexity → Worse R²
   • Less regularization (↓α) → Higher complexity → Similar to Linear Reg
   • For this dataset: Complex models > Regularized simple models

5️⃣ NEXT STEPS:
   • Try Polynomial degree 3 with Ridge
   • Explore feature engineering
   • Use ensemble methods (Random Forest, XGBoost)
   • Cross-validation for robust evaluation
"""

print(recommendations)
print("="*80)
print("\n🎓 Analysis Complete! Check the visualizations above.")
print("="*80)
