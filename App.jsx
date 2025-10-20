import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [sensorData, setSensorData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/sensor_data");
        const data = await res.json();
        setSensorData(data);
      } catch (err) {
        console.error("Error fetching sensor data:", err);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 3000); // refresh every 3 sec
    return () => clearInterval(interval);
  }, []);

  if (!sensorData) {
    return <h3>Loading sensor data...</h3>;
  }

  return (
    <div className="dashboard">
      <h1>🌿 EcoSynth Dashboard</h1>
      <p>Live environmental readings from the backend agent.</p>

      <div className="card">
        <p><strong>Timestamp:</strong> {sensorData.timestamp}</p>
        <p><strong>Temperature:</strong> {sensorData.temperature.toFixed(2)} °C</p>
        <p><strong>Humidity:</strong> {sensorData.humidity.toFixed(2)} %</p>
        <p><strong>Air Quality:</strong> {sensorData.air_quality.toFixed(2)} AQI</p>
        <p><strong>Noise:</strong> {sensorData.noise.toFixed(2)} dB</p>
      </div>
    </div>
  );
}

export default App;

