
import { useState } from "react";
import "./App.css";
function App() {
  const [activeTab, setActiveTab] = useState("Length");
  const [value, setValue] = useState("");
  const [unit1, setUnit1] = useState("");
  const [unit2, setUnit2] = useState("");
  const [result, setResult] = useState("");

  const units = {
    Length: ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"],
    Weight: ["kilograms", "grams", "milligrams", "pounds", "ounces"],
    Temperature: ["celsius", "fahrenheit", "kelvin"],
  };

  const currentUnits = units[activeTab as keyof typeof units];
  async function handleConvert() {
  if (!value || !unit1 || !unit2) {
    alert("Please fill all fields");
    return;
  }

  const endpoints = {
    Length: "length",
    Weight: "weight",
    Temperature: "temperature",
  };

  const endpoint = endpoints[activeTab as keyof typeof endpoints];

  const parameter = activeTab.toLowerCase();

  const params = new URLSearchParams({
    [parameter]: value,
    unit1: unit1,
    unit2: unit2,
  });

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/${endpoint}?${params}`
    );

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail?.message || "Conversion failed");
    }

    const converted =
      data.converted_length ??
      data.converted_weight ??
      data.converted_temperature;

    setResult(`${Number(converted.toFixed(2))} ${unit2}`);

  } catch (error) {
    alert(error instanceof Error ? error.message : "Something went wrong");
  }
}
  function handleTabChange(tab: string) {
    setActiveTab(tab);
    setValue("");
    setUnit1("");
    setUnit2("");
  }

  return (
    <div className="container">
      <h1>Unit Converter</h1>

      <nav>
        <button className={activeTab === "Length" ? "active" : ""} onClick={() => handleTabChange("Length")}>Length</button>
        <button className={activeTab === "Weight" ? "active" : ""} onClick={() => handleTabChange("Weight")}>Weight</button>
        <button className={activeTab === "Temperature" ? "active" : ""} onClick={() => handleTabChange("Temperature")}>Temperature</button>
      </nav>

      <h2>{activeTab} Converter</h2>

      <div className="form-group">
        <label>Enter value</label>
        <input
          type="number"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder="Enter a value"
        />
      </div>

      <div className="form-group">
        <label>Unit to Convert from</label>
        <select value={unit1} onChange={(e) => setUnit1(e.target.value)}>
          <option value="">Select unit</option>
          {currentUnits.map((unit) => (
            <option key={unit} value={unit}>{unit}</option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label>Unit to Convert to</label>
        <select value={unit2} onChange={(e) => setUnit2(e.target.value)}>
          <option value="">Select unit</option>
          {currentUnits.map((unit) => (
            <option key={unit} value={unit}>{unit}</option>
          ))}
        </select>
      </div>

      <button className="convert-btn" onClick={handleConvert}>
        Convert
      </button>
      <div className="result">
        Result: {result}
      </div>
    </div>
  );
}

export default App;
