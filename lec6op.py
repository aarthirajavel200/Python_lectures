import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# Read data
df = pd.read_csv("C:\\Users\\ADMIN\\Downloads\\quikr_car.csv")
duplicates_df = df.duplicated()  # Store duplicates check in a separate variable
print(duplicates_df)

# Dropping the duplicates (if any)
df = df.drop_duplicates()
df1 = df.dropna()
print(df1)

# One hot encoding (if applicable, or label encoding here)
# Apply label encoding to categorical columns
label_encoder1 = LabelEncoder()

# Assuming there are categorical columns like 'Fuel_Type' and 'Transmission' to encode
df1['Fuel_Type'] = label_encoder1.fit_transform(df1['fuel_type'])
print(df1)

# Removing trailing spaces
df1.columns = df1.columns.astype(str).str.strip()

# Print column names after stripping
print("\nAfter stripping:")
print(df1.columns)
df1.loc[:, 'Price'] = df1['Price'].replace('AskForPrice', '0')  # Replace 'AskForPrice' with '0'
df1.loc[:, 'Price'] = pd.to_numeric(df1['Price'], errors='coerce')  # Convert to numeric
df1.loc[:, 'name'] = df1['name'].str.replace(" ", "").str.replace(",", "")
df1.loc[:, 'company'] = df1['company'].str.replace(" ", "").str.replace(",", "")
df1.loc[:, 'kms_driven'] = df1['kms_driven'].str.replace(" kms", "").str.replace(",", "").replace({"Petrol": 0, "Diesel": 1})
df1.loc[:, 'kms_driven'] = pd.to_numeric(df1['kms_driven'], errors='coerce')  # Convert to numeric

# Initialize label enco
le = LabelEncoder()

# Encode all categorical columns in the dataframe
# Assuming columns like 'Car_Name', 'Fuel_Type', etc. need encoding
categorical_columns = ['fuel_type']

# Apply label encoding to these columns
for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

# Features (X) and target (y)
X = df.drop(columns=["name","company","Price"])  # Drop target column
y = df["Price"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.dtypes)


# Initialize model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")
