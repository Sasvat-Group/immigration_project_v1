import { ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle, } from "chart.js"
import { Chart as ChartJS } from "chart.js"
// import ApexCharts from 'apexcharts'
ChartJS.register(
    ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle)

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
}

export const currentYearData = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

    datasets: [

        {
            label: "Current Year",
            data: [32, 38, 43],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "#6259ca",
            pointBackgroundColor: "#ffffff",
            pointRadius: 0,
            fill: true,
            tension: 0.4,
        }, {
            label: "2022",
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
}

// ------------ New Graph ------------

export const linechart = {
    labels: ["2015", "2016", "2017", "2018", "2019", "2020", "2021"],
    datasets: [
        {
            label: "Initiated",
            data: [32, 38, 43],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "#6259ca",
            pointBackgroundColor: "ffffff",
            pointRadius: 0,
            type: "line",
            tension: 0.4,
        },
        {
            label: "Filed",
            data: [30, 35, 40,
                45, 47, 48,
                50, 52, 53,
                55, 60, 65],
            borderWidth: 3,
            backgroundColor: "transparent",
            borderColor: "#01b8ff",
            pointBackgroundColor: "#ffffff",
            pointRadius: 0,
            type: "line",
            // borderDash: [7, 3],
            tension: 0.4,
        },
    ],
}

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

export const linechart1 = {
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

export const linechartoptions1 = {
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


// Bar-chart 1
export const Barchart1 = {
    responsive: true,
    maintainAspectRatio: false,

    plugins: {
        legend: {
            position: "top",
        },
        title: {
            display: false,
            text: "Chart.js Line Chart",
        },
    },
}
export const barchart1data = {
    labels: ["2019", "2020", "2021", "2022"],
    datasets: [
        {
            // label: "My First Dataset",
            data: [200, 450, 290, 367, 256, 543, 345],
            borderWidth: 2,
            backgroundColor: "#9877f9",
            borderColor: "#9877f9",
            pointBackgroundColor: "#ffffff",
            label: "Spend",
        },
    ],
}