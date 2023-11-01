import { ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle, } from "chart.js"
import { Chart as ChartJS } from "chart.js"
// import ApexCharts from 'apexcharts'
ChartJS.register(
    ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle)

// ------------ New Graph ------------

export const linechart = (filed, initiated) => {

    let _filed = filed.map(x => x.TotalCount) || []
    let _initiated = initiated.map(x => x.TotalCount) || []

    let _years = filed.map(x => x.Year).sort() || []

    return {
        labels: _years,
        datasets: [
            {
                label: "Initiated",
                data: _filed,
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
                data: _initiated,
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
export const barchart1data = (data) => {

    let _years = data?.map(x => x.Year).sort() || []
    let _data = data?.map(x => x.BillingAmount).sort() || []

    return {
        labels: _years,
        datasets: [
            {
                // label: "My First Dataset",
                data: _data,
                borderWidth: 2,
                backgroundColor: "#9877f9",
                borderColor: "#9877f9",
                pointBackgroundColor: "#ffffff",
                label: "Spend",
            },
        ],
    }
}