import { ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle, } from "chart.js";
import { Chart as ChartJS } from "chart.js";

ChartJS.register(
    ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle);

export const currentYearOptions = {
    responsive: true,
    maintainAspectRatio: false,

    layout: {
        padding: {
            left: 20,
            right: 20,
        }
    },

    plugins: {
        legend: {
            position: "top",
            display: true,
        },
        scales: {
            x: {},
            y:
            {
                ticks: {
                    min: 0,
                    max: 250,
                    stepSize: 50,
                },
                scaleLabel: {
                    display: true,
                    labelString: "Thousands",
                    fontColor: "transparent",
                },
            },
        },
    },
};
export const currentYearData = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

    datasets: [

        {
            label: "Project Type",
            data: [32, 38, 43],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "#6259ca",
            pointBackgroundColor: "#ffffff",
            pointRadius: 0,
            fill: true,
            tension: 0.4,
        }, {
            label: "Secondary Project Status",
            data: [30, 35, 40,
                45, 47, 48,
                50, 52, 53,
                55, 60, 65],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "rgba(183, 179, 220,0.7)",
            pointBackgroundColor: "#ffffff",
            pointRadius: 0,
            borderDash: [8, 3],
            fill: true,
            tension: 0.4,
        }
    ],
};