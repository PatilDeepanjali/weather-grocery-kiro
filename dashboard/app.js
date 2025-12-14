let tempChartInstance = null;
let trendChartInstance = null;

async function load() {
    const resp = await fetch("data.json");
    const j = await resp.json();

    /* =========================
       WEATHER CHART
    ========================== */
    const weather = j.weather;
    const times = weather.map(w => w.dt);
    const temps = weather.map(w => w.temp);
    const pops = weather.map(w => w.pop * 100);

    const ctx = document.getElementById("tempChart").getContext("2d");
    if (tempChartInstance) tempChartInstance.destroy();

    tempChartInstance = new Chart(ctx, {
        type: "line",
        data: {
            labels: times,
            datasets: [
                {
                    label: "Temperature (°C)",
                    data: temps,
                    borderWidth: 3,
                    tension: 0.35,
                    pointRadius: 3,
                    fill: false
                },
                {
                    label: "Rain Probability (%)",
                    data: pops,
                    borderWidth: 3,
                    tension: 0.35,
                    pointRadius: 3,
                    yAxisID: "y1",
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: "index",
                intersect: false
            },
            animation: {
                duration: 1200,
                easing: "easeOutQuart"
            },
            plugins: {
                legend: {
                    labels: {
                        usePointStyle: true,
                        boxWidth: 8
                    }
                },
                tooltip: {
                    backgroundColor: "rgba(15,23,42,0.9)",
                    titleColor: "#ffffff",
                    bodyColor: "#e5e7eb",
                    cornerRadius: 8
                }
            },
            scales: {
                y: {
                    title: {
                        display: true,
                        text: "Temperature (°C)"
                    }
                },
                y1: {
                    position: "right",
                    grid: { drawOnChartArea: false },
                    title: {
                        display: true,
                        text: "Rain Probability (%)"
                    }
                }
            }
        }
    });

    /* =========================
       GROCERY TRENDS CHART
    ========================== */
    const trends = j.trends;
    const tlabels = trends.map(t => t.date);
    const noodle = trends.map(t => t.metrics.noodles);

    const ctx2 = document.getElementById("trendChart").getContext("2d");
    if (trendChartInstance) trendChartInstance.destroy();

    trendChartInstance = new Chart(ctx2, {
        type: "line",
        data: {
            labels: tlabels,
            datasets: [
                {
                    label: "Noodles Interest",
                    data: noodle,
                    borderWidth: 3,
                    tension: 0.35,
                    pointRadius: 4,
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 1200,
                easing: "easeOutQuart"
            },
            plugins: {
                legend: {
                    labels: {
                        usePointStyle: true
                    }
                },
                tooltip: {
                    backgroundColor: "rgba(15,23,42,0.9)"
                }
            },
            scales: {
                y: {
                    title: {
                        display: true,
                        text: "Interest Score"
                    }
                }
            }
        }
    });

    /* =========================
       INSIGHTS
    ========================== */
    const corr = j.correlations;

    let insights = "<h3>📊 Insights</h3>";

    function explain(val, text) {
        if (val === null || val === undefined) return "";
        return `<p>• ${text} (corr: <b>${val.toFixed(2)}</b>)</p>`;
    }

    insights += explain(corr.temp_cold_drink, "Hotter days increase cold drink demand");
    insights += explain(corr.rain_soup, "Rainy days increase soup demand");
    insights += explain(corr.temp_noodles, "Temperature affects noodles demand");

    let recommendations = "<h3>✅ Recommendations</h3>";
    recommendations += "<p>• Stock more cold drinks during hotter days</p>";
    recommendations += "<p>• Promote soup items during rainy periods</p>";
    recommendations += "<p>• Adjust snack inventory based on temperature trends</p>";

    document.getElementById("insightText").innerHTML = insights + recommendations;
}

/* =========================
   RUN AFTER DOM LOAD
========================== */
document.addEventListener("DOMContentLoaded", load);
