import React from "react";
import { ZoomableGroup, ComposableMap, Geographies, Geography, Graticule, } from "react-simple-maps";
import { ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle, } from "chart.js";
import { Chart as ChartJS } from "chart.js";
// import ApexCharts from 'apexcharts'
ChartJS.register(
  ArcElement, LineElement, BarElement, PointElement, BarController, BubbleController, DoughnutController, LineController, PieController, PolarAreaController, RadarController, ScatterController, CategoryScale, LinearScale, LogarithmicScale, RadialLinearScale, TimeScale, TimeSeriesScale, Decimation, Filler, Legend, Title, Tooltip, SubTitle);

//
export const Dashboard1 = {
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
    tooltip: {
      enabled: true,
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
export const dashboard1 = {
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

  datasets: [
    {
      label: "Filed",
      data: [30, 150, 65, 160, 70, 130, 70, 120, 65, 160, 70, 50],
      borderWidth: 3,
      backgroundColor: "transparent",
      borderColor: "#8ac926",
      pointBackgroundColor: "#ffffff",
      pointRadius: 0,
      borderDash: [0],
      fill: true,
      tension: 0.4,
    },
    {
      label: "Open",
      data: [50, 90, 210, 90, 150, 75, 200, 70, 90, 210, 90, 150, 75],
      borderWidth: 3,
      backgroundColor: "transparent",
      borderColor: "#ffba08",
      pointBackgroundColor: "#ffffff",
      pointRadius: 0,
      fill: true,
      tension: 0.4,
    }, {
      label: "Initiated",
      data: [55, 60, 110, 60, 120, 45, 100, 50, 60, 110, 60, 20],
      borderWidth: 3,
      backgroundColor: "transparent",
      borderColor: "#6259ca",
      pointBackgroundColor: "#ffffff",
      pointRadius: 0,
      fill: true,
      tension: 0.4,
    },
  ],
};

export const radialbarchart = {
  series: [83],
  options: {
    chart: {
      height: 256,
      innerWidth: 100,
      type: "radialBar",
      offsetY: -40,
    },
    plotOptions: {
      radialBar: {
        startAngle: -125,
        endAngle: 105,
        dataLabels: {
          name: {
            fontSize: "16px",
            color: undefined,
            offsetY: 30,
          },
          hollow: {
            size: "60%",
          },
          value: {
            offsetY: -10,
            fontSize: "22px",
            color: undefined,
            formatter: function (val) {
              return val + "%";
            },
          },
        },
      },
    },
    fill: {
      type: "gradient",
      gradient: {
        shade: "dark",
        type: "horizontal",
        shadeIntensity: 0.5,
        gradientToColors: ["#6259ca"],
        inverseColors: !0,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 100],
      },
    },
    stroke: {
      dashArray: 4,
    },
    labels: [""],
    colors: ["#6259ca"],
  },
};

// Map
const geoUrl =
{
  "type": "Topology",
  "objects": {
    "world": {
      "type": "GeometryCollection",
      "geometries": [
        {
          "type": "Polygon",
          "arcs": [[0, 1, 2, 3, 4, 5]],
          "id": "AFG",
          "properties": { "name": "Afghanistan" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[6, 7, 8, 9]], [[10, 11, 12]]],
          "id": "AGO",
          "properties": { "name": "Angola" }
        },
        {
          "type": "Polygon",
          "arcs": [[13, 14, 15, 16, 17]],
          "id": "ALB",
          "properties": { "name": "Albania" }
        },
        {
          "type": "Polygon",
          "arcs": [[18, 19, 20, 21, 22]],
          "id": "ARE",
          "properties": { "name": "United Arab Emirates" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[23, 24]], [[25, 26, 27, 28, 29, 30]]],
          "id": "ARG",
          "properties": { "name": "Argentina" }
        },
        {
          "type": "Polygon",
          "arcs": [[31, 32, 33, 34, 35]],
          "id": "ARM",
          "properties": { "name": "Armenia" }
        },
        {
          "type": "Polygon",
          "arcs": [[36]],
          "id": "ATF",
          "properties": { "name": "French Southern Territories" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[37]], [[38]]],
          "id": "AUS",
          "properties": { "name": "Australia" }
        },
        {
          "type": "Polygon",
          "arcs": [[39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]],
          "id": "AUT",
          "properties": { "name": "Austria" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[50, -35]], [[51, 52, -33, 53, 54]]],
          "id": "AZE",
          "properties": { "name": "Azerbaijan" }
        },
        {
          "type": "Polygon",
          "arcs": [[55, 56, 57, 58]],
          "id": "BDI",
          "properties": { "name": "Burundi" }
        },
        {
          "type": "Polygon",
          "arcs": [[59, 60, 61, 62, 63]],
          "id": "BEL",
          "properties": { "name": "Belgium" }
        },
        {
          "type": "Polygon",
          "arcs": [[64, 65, 66, 67, 68]],
          "id": "BEN",
          "properties": { "name": "Benin" }
        },
        {
          "type": "Polygon",
          "arcs": [[69, 70, 71, -67, 72, 73]],
          "id": "BFA",
          "properties": { "name": "Burkina Faso" }
        },
        {
          "type": "Polygon",
          "arcs": [[74, 75, 76]],
          "id": "BGD",
          "properties": { "name": "Bangladesh" }
        },
        {
          "type": "Polygon",
          "arcs": [[77, 78, 79, 80, 81, 82]],
          "id": "BGR",
          "properties": { "name": "Bulgaria" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[83]], [[84]], [[85]]],
          "id": "BHS",
          "properties": { "name": "Bahamas" }
        },
        {
          "type": "Polygon",
          "arcs": [[86, 87, 88, 89]],
          "id": "BIH",
          "properties": { "name": "Bosnia and Herzegovina" }
        },
        {
          "type": "Polygon",
          "arcs": [[90, 91, 92, 93, 94, 95, 96, 97]],
          "id": "BLR",
          "properties": { "name": "Belarus" }
        },
        {
          "type": "Polygon",
          "arcs": [[98, 99, 100]],
          "id": "BLZ",
          "properties": { "name": "Belize" }
        },
        {
          "type": "Polygon",
          "arcs": [[101, 102, 103, 104, -31]],
          "id": "BOL",
          "properties": { "name": "Bolivia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-27, 105, -104, 106, 107, 108, 109, 110, 111, 112, 113]],
          "id": "BRA",
          "properties": { "name": "Brazil" }
        },
        {
          "type": "Polygon",
          "arcs": [[114, 115]],
          "id": "BRN",
          "properties": { "name": "Brunei" }
        },
        {
          "type": "Polygon",
          "arcs": [[116, 117]],
          "id": "BTN",
          "properties": { "name": "Bhutan" }
        },
        {
          "type": "Polygon",
          "arcs": [[118, 119, 120, 121]],
          "id": "BWA",
          "properties": { "name": "Botswana" }
        },
        {
          "type": "Polygon",
          "arcs": [[122, 123, 124, 125, 126, 127, 128]],
          "id": "CAF",
          "properties": { "name": "Central African Republic" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[129]],
            [[130]],
            [[131]],
            [[132]],
            [[133]],
            [[134]],
            [[135]],
            [[136]],
            [[137]],
            [[138]],
            [[139, 140, 141, 142, 143, 144]],
            [[145]],
            [[146]],
            [[147]],
            [[148]],
            [[149]],
            [[150]],
            [[151]],
            [[152]],
            [[153]],
            [[154]],
            [[155]],
            [[156]],
            [[157]],
            [[158]],
            [[159]],
            [[160]],
            [[161]],
            [[162]],
            [[163]]
          ],
          "id": "CAN",
          "properties": { "name": "Canada" }
        },
        {
          "type": "Polygon",
          "arcs": [[-47, 164, 165, 166, -43, 167, 168, 169]],
          "id": "CHE",
          "properties": { "name": "Switzerland" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[-24, 170]], [[-30, 171, 172, -102]]],
          "id": "CHL",
          "properties": { "name": "Chile" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[173]],
            [
              [
                174,
                175,
                176,
                177,
                178,
                179,
                180,
                181,
                182,
                183,
                184,
                185,
                186,
                187,
                -118,
                188,
                189,
                190,
                191,
                -4,
                192,
                193,
                194,
                195,
                196,
                197,
                198,
                199,
                200,
                201,
                202
              ]
            ]
          ],
          "id": "CHN",
          "properties": { "name": "China" }
        },
        {
          "type": "Polygon",
          "arcs": [[203, 204, 205, 206, -70, 207]],
          "id": "CIV",
          "properties": { "name": "Cote d'Ivoire" }
        },
        {
          "type": "Polygon",
          "arcs": [[208, 209, 210, 211, 212, 213, 214, -129, 215]],
          "id": "CMR",
          "properties": { "name": "Cameroon" }
        },
        {
          "type": "Polygon",
          "arcs": [
            [
              216,
              217,
              218,
              219,
              -56,
              220,
              221,
              222,
              -10,
              223,
              -13,
              224,
              -127,
              225,
              226
            ]
          ],
          "id": "COD",
          "properties": { "name": "Democratic Republic of Congo" }
        },
        {
          "type": "Polygon",
          "arcs": [[-12, 227, 228, -216, -128, -225]],
          "id": "COG",
          "properties": { "name": "Congo" }
        },
        {
          "type": "Polygon",
          "arcs": [[229, 230, 231, 232, 233, -108, 234]],
          "id": "COL",
          "properties": { "name": "Colombia" }
        },
        {
          "type": "Polygon",
          "arcs": [[235, 236, 237, 238]],
          "id": "CRI",
          "properties": { "name": "Costa Rica" }
        },
        {
          "type": "Polygon",
          "arcs": [[239]],
          "id": "CUB",
          "properties": { "name": "Cuba" }
        },
        {
          "type": "Polygon",
          "arcs": [[240]],
          "id": "CYP",
          "properties": { "name": "Cyprus" }
        },
        {
          "type": "Polygon",
          "arcs": [[-49, 241, 242, 243]],
          "id": "CZE",
          "properties": { "name": "Czechia" }
        },
        {
          "type": "Polygon",
          "arcs": [[244, 245, -242, -48, -170, 246, 247, -61, 248, 249, 250]],
          "id": "DEU",
          "properties": { "name": "Germany" }
        },
        {
          "type": "Polygon",
          "arcs": [[251, 252, 253, 254]],
          "id": "DJI",
          "properties": { "name": "Djibouti" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[255]], [[-251, 256]]],
          "id": "DNK",
          "properties": { "name": "Denmark" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[257]]],
          "id": "GRL",
          "properties": { "name": "Greenland" }
        },
        {
          "type": "Polygon",
          "arcs": [[258, 259]],
          "id": "DOM",
          "properties": { "name": "Dominican Republic" }
        },
        {
          "type": "Polygon",
          "arcs": [[260, 261, 262, 263, 264, 265, 266, 267]],
          "id": "DZA",
          "properties": { "name": "Algeria" }
        },
        {
          "type": "Polygon",
          "arcs": [[268, -230, 269]],
          "id": "ECU",
          "properties": { "name": "Ecuador" }
        },
        {
          "type": "Polygon",
          "arcs": [[270, 271, 272]],
          "id": "EGY",
          "properties": { "name": "Egypt" }
        },
        {
          "type": "Polygon",
          "arcs": [[273, 274, 275, 276, 277, 278, 279, -255]],
          "id": "ERI",
          "properties": { "name": "Eritrea" }
        },
        {
          "type": "Polygon",
          "arcs": [[280, 281, 282, 283]],
          "id": "ESP",
          "properties": { "name": "Spain" }
        },
        {
          "type": "Polygon",
          "arcs": [[284, 285, 286, 287]],
          "id": "EST",
          "properties": { "name": "Estonia" }
        },
        {
          "type": "Polygon",
          "arcs": [
            [288, 289, -274, -254, 290, 291, 292, 293, 294, 295, 296, 297, -277]
          ],
          "id": "ETH",
          "properties": { "name": "Ethiopia" }
        },
        {
          "type": "Polygon",
          "arcs": [[298, 299, 300, 301]],
          "id": "FIN",
          "properties": { "name": "Finland" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[302]], [[303]], [[304]]],
          "id": "FJI",
          "properties": { "name": "Fiji" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[305]], [[306, -247, -169, 307, 308, -282, 309, -63]]],
          "id": "FRA",
          "properties": { "name": "France" }
        },
        {
          "type": "Polygon",
          "arcs": [[310, 311, 312, -112]],
          "id": "GUF",
          "properties": { "name": "French Guiana" }
        },
        {
          "type": "Polygon",
          "arcs": [[313, 314, -209, -229]],
          "id": "GAB",
          "properties": { "name": "Gabon" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[315, 316]], [[317]]],
          "id": "GBR",
          "properties": { "name": "United Kingdom" }
        },
        {
          "type": "Polygon",
          "arcs": [[318, 319, 320, 321, 322, -54, -32, 323]],
          "id": "GEO",
          "properties": { "name": "Georgia" }
        },
        {
          "type": "Polygon",
          "arcs": [[324, -208, -74, 325]],
          "id": "GHA",
          "properties": { "name": "Ghana" }
        },
        {
          "type": "Polygon",
          "arcs": [[326, 327, 328, 329, 330, 331, -206]],
          "id": "GIN",
          "properties": { "name": "Guinea" }
        },
        {
          "type": "Polygon",
          "arcs": [[332, 333]],
          "id": "GMB",
          "properties": { "name": "Gambia" }
        },
        {
          "type": "Polygon",
          "arcs": [[334, 335, -330]],
          "id": "GNB",
          "properties": { "name": "Guinea-Bissau" }
        },
        {
          "type": "Polygon",
          "arcs": [[336, -210, -315]],
          "id": "GNQ",
          "properties": { "name": "Equatorial Guinea" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[337]], [[338, -14, 339, -81, 340]]],
          "id": "GRC",
          "properties": { "name": "Greece" }
        },
        {
          "type": "Polygon",
          "arcs": [[341, 342, -101, 343, 344, 345]],
          "id": "GTM",
          "properties": { "name": "Guatemala" }
        },
        {
          "type": "Polygon",
          "arcs": [[346, 347, -110, 348]],
          "id": "GUY",
          "properties": { "name": "Guyana" }
        },
        {
          "type": "Polygon",
          "arcs": [[349, 350, -345, 351, 352]],
          "id": "HND",
          "properties": { "name": "Honduras" }
        },
        {
          "type": "Polygon",
          "arcs": [[353, 354, 355, -90, 356, 357, 358]],
          "id": "HRV",
          "properties": { "name": "Croatia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-260, 359]],
          "id": "HTI",
          "properties": { "name": "Haiti" }
        },
        {
          "type": "Polygon",
          "arcs": [[-40, 360, 361, 362, 363, 364, -359, 365]],
          "id": "HUN",
          "properties": { "name": "Hungary" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[366]],
            [[367, 368]],
            [[369]],
            [[370]],
            [[371]],
            [[372]],
            [[373]],
            [[374]],
            [[375, 376]],
            [[377]],
            [[378]],
            [[379, 380]],
            [[381]]
          ],
          "id": "IDN",
          "properties": { "name": "Indonesia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-191, 382, -189, -117, -188, 383, -77, 384, 385]],
          "id": "IND",
          "properties": { "name": "India" }
        },
        {
          "type": "Polygon",
          "arcs": [[386, -316]],
          "id": "IRL",
          "properties": { "name": "Ireland" }
        },
        {
          "type": "Polygon",
          "arcs": [[387, -6, 388, 389, 390, 391, 392, -51, -34, -53, 393]],
          "id": "IRN",
          "properties": { "name": "Iran" }
        },
        {
          "type": "Polygon",
          "arcs": [[-391, 394, 395, 396, 397, 398, 399, 400]],
          "id": "IRQ",
          "properties": { "name": "Iraq" }
        },
        {
          "type": "Polygon",
          "arcs": [[401]],
          "id": "ISL",
          "properties": { "name": "Iceland" }
        },
        {
          "type": "Polygon",
          "arcs": [[402, 403, 404, 405, 406, 407]],
          "id": "ISR",
          "properties": { "name": "Israel" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[408]], [[409]], [[410, 411, -308, -168, -42]]],
          "id": "ITA",
          "properties": { "name": "Italy" }
        },
        {
          "type": "Polygon",
          "arcs": [[412]],
          "id": "JAM",
          "properties": { "name": "Jamaica" }
        },
        {
          "type": "Polygon",
          "arcs": [[-403, 413, -398, 414, 415, -405, 416]],
          "id": "JOR",
          "properties": { "name": "Jordan" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[417]], [[418]], [[419]]],
          "id": "JPN",
          "properties": { "name": "Japan" }
        },
        {
          "type": "Polygon",
          "arcs": [
            [
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              -195,
              433
            ]
          ],
          "id": "KAZ",
          "properties": { "name": "Kazakhstan" }
        },
        {
          "type": "Polygon",
          "arcs": [[434, 435, 436, 437, -295, 438]],
          "id": "KEN",
          "properties": { "name": "Kenya" }
        },
        {
          "type": "Polygon",
          "arcs": [[-434, -194, 439, 440]],
          "id": "KGZ",
          "properties": { "name": "Kyrgyzstan" }
        },
        {
          "type": "Polygon",
          "arcs": [[441, 442, 443, 444]],
          "id": "KHM",
          "properties": { "name": "Cambodia" }
        },
        {
          "type": "Polygon",
          "arcs": [[445, 446]],
          "id": "KOR",
          "properties": { "name": "South Korea" }
        },
        {
          "type": "Polygon",
          "arcs": [[447, 448, 449, 450, 451]],
          "id": "XXK",
          "properties": { "name": "Kosovo" }
        },
        {
          "type": "Polygon",
          "arcs": [[452, 453, -396]],
          "id": "KWT",
          "properties": { "name": "Kuwait" }
        },
        {
          "type": "Polygon",
          "arcs": [[454, 455, -186, 456, -443]],
          "id": "LAO",
          "properties": { "name": "Laos" }
        },
        {
          "type": "Polygon",
          "arcs": [[-407, 457, 458]],
          "id": "LBN",
          "properties": { "name": "Lebanon" }
        },
        {
          "type": "Polygon",
          "arcs": [[459, 460, -327, -205]],
          "id": "LBR",
          "properties": { "name": "Liberia" }
        },
        {
          "type": "Polygon",
          "arcs": [[461, -268, 462, 463, -272, 464, 465]],
          "id": "LBY",
          "properties": { "name": "Libya" }
        },
        {
          "type": "Polygon",
          "arcs": [[466]],
          "id": "LKA",
          "properties": { "name": "Sri Lanka" }
        },
        {
          "type": "Polygon",
          "arcs": [[467]],
          "id": "LSO",
          "properties": { "name": "Lesotho" }
        },
        {
          "type": "Polygon",
          "arcs": [[468, 469, 470, -91, 471]],
          "id": "LTU",
          "properties": { "name": "Lithuania" }
        },
        {
          "type": "Polygon",
          "arcs": [[-248, -307, -62]],
          "id": "LUX",
          "properties": { "name": "Luxembourg" }
        },
        {
          "type": "Polygon",
          "arcs": [[472, -288, 473, -92, -471]],
          "id": "LVA",
          "properties": { "name": "Latvia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-265, 474, 475]],
          "id": "MAR",
          "properties": { "name": "Morocco" }
        },
        {
          "type": "Polygon",
          "arcs": [[476, 477]],
          "id": "MDA",
          "properties": { "name": "Moldova" }
        },
        {
          "type": "Polygon",
          "arcs": [[478]],
          "id": "MDG",
          "properties": { "name": "Madagascar" }
        },
        {
          "type": "Polygon",
          "arcs": [[-99, -343, 479, 480, 481]],
          "id": "MEX",
          "properties": { "name": "Mexico" }
        },
        {
          "type": "Polygon",
          "arcs": [[-452, 482, -82, -340, 483]],
          "id": "MKD",
          "properties": { "name": "North Macedonia" }
        },
        {
          "type": "Polygon",
          "arcs": [[484, -262, 485, -71, -207, -332, 486]],
          "id": "MLI",
          "properties": { "name": "Mali" }
        },
        {
          "type": "Polygon",
          "arcs": [[487, -75, -384, -187, -456, 488]],
          "id": "MMR",
          "properties": { "name": "Myanmar" }
        },
        {
          "type": "Polygon",
          "arcs": [[489, -89, 490, -450, -16]],
          "id": "MNE",
          "properties": { "name": "Montenegro" }
        },
        {
          "type": "Polygon",
          "arcs": [[491, 492, 493, 494, 495, 496, 497, 498, -197]],
          "id": "MNG",
          "properties": { "name": "Mongolia" }
        },
        {
          "type": "Polygon",
          "arcs": [[499, 500, 501, 502, 503, 504, 505, 506, 507]],
          "id": "MOZ",
          "properties": { "name": "Mozambique" }
        },
        {
          "type": "Polygon",
          "arcs": [[508, 509, 510, -263, -485]],
          "id": "MRT",
          "properties": { "name": "Mauritania" }
        },
        {
          "type": "Polygon",
          "arcs": [[-508, 511, 512, 513]],
          "id": "MWI",
          "properties": { "name": "Malawi" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[514, 515, 516, 517]], [[-380, 518, -116, 519]]],
          "id": "MYS",
          "properties": { "name": "Malaysia" }
        },
        {
          "type": "Polygon",
          "arcs": [[520, -8, 521, -120, 522]],
          "id": "NAM",
          "properties": { "name": "Namibia" }
        },
        {
          "type": "Polygon",
          "arcs": [[523]],
          "id": "NCL",
          "properties": { "name": "New Caledonia" }
        },
        {
          "type": "Polygon",
          "arcs": [
            [-72, -486, -261, -462, 524, 525, 526, 527, 528, -213, 529, -68]
          ],
          "id": "NER",
          "properties": { "name": "Niger" }
        },
        {
          "type": "Polygon",
          "arcs": [[530, -69, -530, -212]],
          "id": "NGA",
          "properties": { "name": "Nigeria" }
        },
        {
          "type": "Polygon",
          "arcs": [[531, -353, 532, -237]],
          "id": "NIC",
          "properties": { "name": "Nicaragua" }
        },
        {
          "type": "Polygon",
          "arcs": [[-249, -60, 533]],
          "id": "NLD",
          "properties": { "name": "Netherlands" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[-302, 534, 535]], [[536]], [[537]], [[538]]],
          "id": "NOR",
          "properties": { "name": "Norway" }
        },
        {
          "type": "Polygon",
          "arcs": [[-383, -190]],
          "id": "NPL",
          "properties": { "name": "Nepal" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[539]], [[540]]],
          "id": "NZL",
          "properties": { "name": "New Zealand" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[541, 542, -22, 543]], [[-20, 544]]],
          "id": "OMN",
          "properties": { "name": "Oman" }
        },
        {
          "type": "Polygon",
          "arcs": [[-192, -386, 545, -389, -5]],
          "id": "PAK",
          "properties": { "name": "Pakistan" }
        },
        {
          "type": "Polygon",
          "arcs": [[546, -239, 547, -232]],
          "id": "PAN",
          "properties": { "name": "Panama" }
        },
        {
          "type": "Polygon",
          "arcs": [[-173, 548, -270, -235, -107, -103]],
          "id": "PER",
          "properties": { "name": "Peru" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[549]],
            [[550]],
            [[551]],
            [[552]],
            [[553]],
            [[554]],
            [[555]]
          ],
          "id": "PHL",
          "properties": { "name": "Philippines" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[556]], [[557]], [[-376, 558]], [[559]]],
          "id": "PNG",
          "properties": { "name": "Papua New Guinea" }
        },
        {
          "type": "Polygon",
          "arcs": [[-246, 560, 561, -472, -98, 562, 563, -243]],
          "id": "POL",
          "properties": { "name": "Poland" }
        },
        {
          "type": "Polygon",
          "arcs": [[564]],
          "id": "PRI",
          "properties": { "name": "Puerto Rico" }
        },
        {
          "type": "Polygon",
          "arcs": [[565, -447, 566, -183]],
          "id": "PRK",
          "properties": { "name": "North Korea" }
        },
        {
          "type": "Polygon",
          "arcs": [[-284, 567]],
          "id": "PRT",
          "properties": { "name": "Portugal" }
        },
        {
          "type": "Polygon",
          "arcs": [[-105, -106, -26]],
          "id": "PRY",
          "properties": { "name": "Paraguay" }
        },
        {
          "type": "Polygon",
          "arcs": [[568, 569]],
          "id": "QAT",
          "properties": { "name": "Qatar" }
        },
        {
          "type": "Polygon",
          "arcs": [[570, -478, 571, 572, -78, 573, -363]],
          "id": "ROU",
          "properties": { "name": "Romania" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[574]],
            [[-562, 575, -469]],
            [[576]],
            [[577]],
            [[578]],
            [[579]],
            [[580]],
            [[581]],
            [[582]],
            [
              [
                -181,
                583,
                584,
                585,
                -177,
                586,
                -175,
                587,
                -202,
                588,
                -200,
                589,
                -198,
                -499,
                590,
                591,
                -496,
                592,
                -494,
                593,
                -492,
                -196,
                -433,
                594,
                -431,
                595,
                596,
                -428,
                597,
                -426,
                598,
                599,
                600,
                -55,
                601,
                -322,
                602,
                -320,
                603,
                604,
                605,
                606,
                607,
                608,
                609,
                610,
                611,
                -95,
                612,
                -93,
                -474,
                -287,
                613,
                614,
                -299,
                615
              ]
            ],
            [[616]],
            [[617]],
            [[618]]
          ],
          "id": "RUS",
          "properties": { "name": "Russia" }
        },
        {
          "type": "Polygon",
          "arcs": [[619, 620, -57, -220, 621]],
          "id": "RWA",
          "properties": { "name": "Rwanda" }
        },
        {
          "type": "Polygon",
          "arcs": [[-475, -264, -511, 622]],
          "id": "ESH",
          "properties": { "name": "Western Sahara" }
        },
        {
          "type": "Polygon",
          "arcs": [[623, -415, -397, -454, 624, -570, 625, -23, -543, 626]],
          "id": "SAU",
          "properties": { "name": "Saudi Arabia" }
        },
        {
          "type": "Polygon",
          "arcs": [
            [627, 628, -124, 629, -465, -271, 630, -279, 631, -298, 632]
          ],
          "id": "SDN",
          "properties": { "name": "Sudan" }
        },
        {
          "type": "Polygon",
          "arcs": [[633, -296, -438, 634, 635, -226, -126, 636, -628]],
          "id": "SSD",
          "properties": { "name": "South Sudan" }
        },
        {
          "type": "Polygon",
          "arcs": [[637, -509, -487, -331, -336, 638, -334]],
          "id": "SEN",
          "properties": { "name": "Senegal" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[639]], [[640]], [[641]], [[642]], [[643]]],
          "id": "SLB",
          "properties": { "name": "Solomon Islands" }
        },
        {
          "type": "Polygon",
          "arcs": [[644, -328, -461]],
          "id": "SLE",
          "properties": { "name": "Sierra Leone" }
        },
        {
          "type": "Polygon",
          "arcs": [[645, -346, -351]],
          "id": "SLV",
          "properties": { "name": "El Salvador" }
        },
        {
          "type": "Polygon",
          "arcs": [[646, 647, -291, -253, 648, -439, -294]],
          "id": "SOM",
          "properties": { "name": "Somalia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-83, -483, -451, -491, -88, 649, -355, 650, -364, -574]],
          "id": "SRB",
          "properties": { "name": "Serbia" }
        },
        {
          "type": "Polygon",
          "arcs": [[651, -312, 652, -111, -348]],
          "id": "SUR",
          "properties": { "name": "Suriname" }
        },
        {
          "type": "Polygon",
          "arcs": [[-564, 653, -361, -50, -244]],
          "id": "SVK",
          "properties": { "name": "Slovakia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-41, -366, -358, 654, -411]],
          "id": "SVN",
          "properties": { "name": "Slovenia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-535, -301, 655]],
          "id": "SWE",
          "properties": { "name": "Sweden" }
        },
        {
          "type": "Polygon",
          "arcs": [[656, -504]],
          "id": "SWZ",
          "properties": { "name": "Eswatini" }
        },
        {
          "type": "Polygon",
          "arcs": [[-414, -408, -459, 657, 658, -399]],
          "id": "SYR",
          "properties": { "name": "Syria" }
        },
        {
          "type": "Polygon",
          "arcs": [[-529, 659, -527, 660, -525, -466, -630, -123, -215, 661]],
          "id": "TCD",
          "properties": { "name": "Chad" }
        },
        {
          "type": "Polygon",
          "arcs": [[662, -326, -73, -66]],
          "id": "TGO",
          "properties": { "name": "Togo" }
        },
        {
          "type": "Polygon",
          "arcs": [[663, -518, 664, -489, -455, -442]],
          "id": "THA",
          "properties": { "name": "Thailand" }
        },
        {
          "type": "Polygon",
          "arcs": [[-440, -193, -3, 665]],
          "id": "TJK",
          "properties": { "name": "Tajikistan" }
        },
        {
          "type": "Polygon",
          "arcs": [[-388, 666, -422, 667, -1]],
          "id": "TKM",
          "properties": { "name": "Turkmenistan" }
        },
        {
          "type": "Polygon",
          "arcs": [[668, -368]],
          "id": "TLS",
          "properties": { "name": "Timor" }
        },
        {
          "type": "Polygon",
          "arcs": [[669]],
          "id": "TTO",
          "properties": { "name": "Trinidad and Tobago" }
        },
        {
          "type": "Polygon",
          "arcs": [[-267, 670, -463]],
          "id": "TUN",
          "properties": { "name": "Tunisia" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[-324, -36, -393, 671, -400, -659, 672]],
            [[-341, -80, 673]]
          ],
          "id": "TUR",
          "properties": { "name": "Turkey" }
        },
        {
          "type": "Polygon",
          "arcs": [[674]],
          "id": "TWN",
          "properties": { "name": "Taiwan" }
        },
        {
          "type": "Polygon",
          "arcs": [
            [
              -436,
              675,
              676,
              -500,
              677,
              678,
              679,
              680,
              -221,
              -59,
              681,
              -620,
              682
            ]
          ],
          "id": "TZA",
          "properties": { "name": "Tanzania" }
        },
        {
          "type": "Polygon",
          "arcs": [[-622, -219, 683, -217, 684, -635, -437, -683]],
          "id": "UGA",
          "properties": { "name": "Uganda" }
        },
        {
          "type": "Polygon",
          "arcs": [
            [
              685,
              -611,
              686,
              -609,
              687,
              688,
              689,
              -605,
              690,
              -572,
              -477,
              -571,
              -362,
              -654,
              -563,
              -97
            ]
          ],
          "id": "UKR",
          "properties": { "name": "Ukraine" }
        },
        {
          "type": "Polygon",
          "arcs": [[-114, 691, -28]],
          "id": "URY",
          "properties": { "name": "Uruguay" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[692]],
            [[693]],
            [[694]],
            [[695]],
            [[696]],
            [[697, -481, 698, -140]],
            [[699]],
            [[700]],
            [[701]],
            [[-144, 702, -142, 703]]
          ],
          "id": "USA",
          "properties": { "name": "United States" }
        },
        {
          "type": "Polygon",
          "arcs": [[-668, -421, -441, -666, -2]],
          "id": "UZB",
          "properties": { "name": "Uzbekistan" }
        },
        {
          "type": "Polygon",
          "arcs": [[704, -349, -109, -234]],
          "id": "VEN",
          "properties": { "name": "Venezuela" }
        },
        {
          "type": "Polygon",
          "arcs": [[705, -444, -457, -185]],
          "id": "VNM",
          "properties": { "name": "Vietnam" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[706]], [[707]]],
          "id": "VUT",
          "properties": { "name": "Vanuatu" }
        },
        {
          "type": "Polygon",
          "arcs": [[-417, -404]],
          "id": "PSX",
          "properties": { "name": "West Bank" }
        },
        {
          "type": "Polygon",
          "arcs": [[708, -627, -542]],
          "id": "YEM",
          "properties": { "name": "Yemen" }
        },
        {
          "type": "Polygon",
          "arcs": [[-523, -119, 709, -505, -657, -503, 710], [-468]],
          "id": "ZAF",
          "properties": { "name": "South Africa" }
        },
        {
          "type": "Polygon",
          "arcs": [[-512, -507, 711, -121, -522, -7, -223, 712, -680]],
          "id": "ZMB",
          "properties": { "name": "Zambia" }
        },
        {
          "type": "Polygon",
          "arcs": [[-710, -122, -712, -506]],
          "id": "ZWE",
          "properties": { "name": "Zimbabwe" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[713]],
            [[714]],
            [[715]],
            [[716]],
            [[717]],
            [[718]],
            [[719]],
            [[720]]
          ],
          "id": "CPV",
          "properties": { "name": "Cape Verde" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[721]], [[722]], [[723]]],
          "id": "COM",
          "properties": { "name": "Comoros" }
        },
        {
          "type": "Polygon",
          "arcs": [[724]],
          "id": "MUS",
          "properties": { "name": "Mauritius" }
        },
        {
          "type": "Polygon",
          "arcs": [[725]],
          "id": "SYC",
          "properties": { "name": "Seychelles" }
        },
        {
          "type": "Polygon",
          "arcs": [[726]],
          "id": "BHR",
          "properties": { "name": "Bahrain" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[727]], [[728]]],
          "id": "MDV",
          "properties": { "name": "Maldives" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[729]], [[730]]],
          "id": "MHL",
          "properties": { "name": "Marshall Islands" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[731]], [[732]], [[733]], [[734]], [[735]]],
          "id": "FSM",
          "properties": { "name": "Micronesia (country)" }
        },
        {
          "type": "Polygon",
          "arcs": [[736]],
          "id": "NRU",
          "properties": { "name": "Nauru" }
        },
        {
          "type": "Polygon",
          "arcs": [[737]],
          "id": "PLW",
          "properties": { "name": "Palau" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[738]], [[739]]],
          "id": "WSM",
          "properties": { "name": "Samoa" }
        },
        {
          "type": "Polygon",
          "arcs": [[515, 740]],
          "id": "SGP",
          "properties": { "name": "Singapore" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[741]], [[742]], [[743]]],
          "id": "TON",
          "properties": { "name": "Tonga" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [
            [[744]],
            [[745]],
            [[746]],
            [[747]],
            [[748]],
            [[749]],
            [[750]]
          ],
          "id": "TUV",
          "properties": { "name": "Tuvalu" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[751]], [[752]]],
          "id": "ATG",
          "properties": { "name": "Antigua and Barbuda" }
        },
        {
          "type": "Polygon",
          "arcs": [[753]],
          "id": "BRB",
          "properties": { "name": "Barbados" }
        },
        {
          "type": "Polygon",
          "arcs": [[754]],
          "id": "DMA",
          "properties": { "name": "Dominica" }
        },
        {
          "type": "Polygon",
          "arcs": [[755]],
          "id": "GRD",
          "properties": { "name": "Grenada" }
        },
        {
          "type": "MultiPolygon",
          "arcs": [[[756]], [[757]]],
          "id": "KNA",
          "properties": { "name": "Saint Kitts and Nevis" }
        },
        {
          "type": "Polygon",
          "arcs": [[758]],
          "id": "LCA",
          "properties": { "name": "Saint Lucia" }
        },
        {
          "type": "Polygon",
          "arcs": [[759]],
          "id": "VCT",
          "properties": { "name": "Saint Vincent and the Grenadines" }
        },
        {
          "type": "Polygon",
          "arcs": [[760]],
          "id": "AND",
          "properties": { "name": "Andorra" }
        },
        {
          "type": "Polygon",
          "arcs": [[-45, 761, -166, 762]],
          "id": "LIE",
          "properties": { "name": "Liechtenstein" }
        },
        {
          "type": "Polygon",
          "arcs": [[763]],
          "id": "MLT",
          "properties": { "name": "Malta" }
        },
        {
          "type": "Polygon",
          "arcs": [[764]],
          "id": "MCO",
          "properties": { "name": "Monaco" }
        },
        {
          "type": "Polygon",
          "arcs": [[765]],
          "id": "SMR",
          "properties": { "name": "San Marino" }
        },
        {
          "type": "Polygon",
          "arcs": [[766]],
          "id": "KIR",
          "properties": { "name": "Kiribati" }
        },
        {
          "type": "Polygon",
          "arcs": [[767]],
          "id": "STP",
          "properties": { "name": "Sao Tome and Principe" }
        }
      ]
    }
  },
  "arcs": [],
  "bbox": [-180, -55.61183, 180, 83.64513]
}
const rounded = (num) => {
  if (num > 1000000000) {
    return Math.round(num / 100000000) / 10 + "Bn";
  } else if (num > 1000000) {
    return Math.round(num / 100000) / 10 + "M";
  } else {
    return Math.round(num / 100) / 10 + "K";
  }
};
export const EDashboardMap = ({ setTooltipContent }) => {
  return (
    <ComposableMap
      data-tip=""
      projectionConfig={{ scale: 200 }}
      className="ht-300 ht-lg-400 mx-auto w-100"
      id="vmap"
    >
      <ZoomableGroup>
        <Graticule stroke="" />
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                onMouseEnter={() => {
                  const { NAME, POP_EST } = geo.properties;
                  setTooltipContent(`${NAME} — ${rounded(POP_EST)}`);
                }}
                onMouseLeave={() => {
                  setTooltipContent("");
                }}
                style={{
                  default: {
                    fill: "#6f42c1",
                    outline: "none",
                  },
                  hover: {
                    fill: "#FF5533",
                    outline: "none",
                  },
                  pressed: {
                    fill: "#E42",
                    outline: "none",
                  },
                }}
              />
            ))
          }
        </Geographies>
      </ZoomableGroup>
    </ComposableMap>
  );
};
