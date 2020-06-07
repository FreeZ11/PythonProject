let prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    let currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
      document.getElementById("navbar").style.top = "0";
    }
    else {
      document.getElementById("navbar").style.top = "-70px";
    }
    prevScrollpos = currentScrollPos;
}

var endpoint = 'api/data/'
var defaultData = []
var defaultDataSubs = []
let channel_views = ""
let channel_name = ""
let channel_videos = ""
let channel_subs = ""
var labels = []

$.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        labels = data.labels
        defaultData = data.values
        defaultDataSubs = data.valuesSubs
        channel_views = data.channel_views
        channel_name = data.channel_name
        channel_videos = data.channel_videos
        channel_subs = data.channel_subs
        setChart()
        setData()
    },
    error: function (error_data) {
        console.log("error")
        console.log(error_data)
    }
})

function setData() {
    document.getElementById('channel_info').innerHTML =
        "<h1 class='channel_results'>Name: " + channel_name + "</h1>"
        + "<h1 class='channel_results'>Views: " + channel_views + "</h1>"
        + "<h1 class='channel_results'>Subs: " + channel_subs + "</h1>"
        + "<h1 class='channel_results'>Videos: " + channel_videos + "</h1>";
}
function setChart() {
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: '# of Views',
                data: defaultData,
                backgroundColor: [
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(0, 128, 0, 0.3)',
                    'rgba(155,135,12,0.59)',

                ],
                borderColor: [
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(37,144,17)',
                    'rgb(208,182,0)',

                ],
                borderWidth: 1
            }],

        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]

            },
            title: {
                display: true,
                text: 'Increase/decrease of views'
            }
        }
    });

var colorChangeValue = 0; //set this to whatever is the deciding color change value
var dataset = myChart.data.datasets[0];
for (var i = 0; i < dataset.data.length-1; i++) {
  if (dataset.data[i] < colorChangeValue) {
    dataset.backgroundColor[i] = 'rgba(135, 0, 0, 0.3)';
    dataset.borderColor[i] = 'rgba(135,0,0,1)';
  }
}
myChart.update();
}