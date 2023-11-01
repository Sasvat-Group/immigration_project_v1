import { ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle, } from "chart.js"
import { Chart as ChartJS } from "chart.js"

ChartJS.register(
    ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle)

// ------------ Dashboard Graphs ------------

const allMonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

export const loadFiledData = ({ previous_filed, this_filed }) => {

    let previous_filed_data = previous_filed.map(x => x.TotalCount)
    let this_filed_data = this_filed.map(x => x.TotalCount)

    return {
        labels: allMonths,
        datasets: [
            {
                label: "2023",
                data: this_filed_data,
                borderWidth: 3,
                backgroundColor: "transparent",
                borderColor: "#6259ca",
                pointBackgroundColor: "ffffff",
                pointRadius: 0,
                type: "line",
                tension: 0.4,
            },
            {
                label: "2022",
                data: previous_filed_data,
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
    }
}

export const loadInitiatedData = ({ previous_initiated, this_initiated }) => {

    let previous_initiated_data = previous_initiated.map(x => x.TotalCount)
    let this_initiated_data = this_initiated.map(x => x.TotalCount)

    return {
        labels: allMonths,
        datasets: [
            {
                label: "2023",
                data: this_initiated_data,
                borderWidth: 3,
                backgroundColor: "transparent",
                borderColor: "#01b8ff",
                pointBackgroundColor: "ffffff",
                pointRadius: 0,
                type: "line",
                tension: 0.4,
            },
            {
                label: "2022",
                data: previous_initiated_data,
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
    }
}


export const caseFiledOptions = {
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
            enabled: true,
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
}

export const caseInitiatedData = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    datasets: [
        {
            label: "2023",
            data: [32, 38, 43],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "#01b8ff",
            pointBackgroundColor: "ffffff",
            pointRadius: 0,
            type: "line",
            tension: 0.4,
        },
        {
            label: "2022",
            data: [30, 35, 40,
                45, 47, 48,
                50, 52, 53,
                55, 60, 65],
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
}
export const caseInitiatedOptions = {
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
            enabled: true,
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
}