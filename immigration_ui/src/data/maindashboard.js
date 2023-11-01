
// Linechart
export const linechart = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Aug", "Sep", "Oct"],
    datasets: [
        {
            label: "TOTAL BUDGET",
            data: [100, 210, 180, 454, 454, 230, 230, 656, 656, 350, 350, 210, 410],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "#6259ca",
            pointBackgroundColor: "ffffff",
            pointRadius: 0,
            type: "line",
            tension: 0.4,
        },
        {
            label: "AMOUNT USED",
            data: [200, 530, 110, 110, 480, 520, 780, 435, 475, 738, 454, 454, 230],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "rgb(183, 179, 220,0.5)",
            pointBackgroundColor: "#ffffff",
            pointRadius: 0,
            type: "line",
            borderDash: [7, 3],
            tension: 0.3,
        },
    ],
};
export const linechartoptions = {
    responsive: true,
    maintainAspectRatio: false,

    plugins: {
        title: {
            display: true,
        },
        legend: {
            position: "top",
            display: true,
        },
        tooltip: {
            enabled: false,
        }
    },
    scales: {
        x: {
            ticks: {
                fontColor: "#c8ccdb",
            },
            barPercentage: 0.7,
            display: true,
            grid: {
                borderColor: 'rgba(119, 119, 142, 0.2)',
            }
        },
        y: {
            display: true,
            grid: {
                borderColor: 'rgba(119, 119, 142, 0.2)',
            },
            scaleLabel: {
                display: true,
                labelString: 'Thousands',
                fontColor: 'transparent'
            }
        }
    },
    interaction: {
        intersect: false,
    },
};
