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
var labels = []

$.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        labels = data.labels
        defaultData = data.values
        defaultDataSubs = data.valuesSubs
        setChart()
    },
    error: function (error_data) {
        console.log("error")
        console.log(error_data)
    }
})


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

            }
        }
    });
    var ctx2 = document.getElementById('myChart2');
    var myChart2 = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: '# of Subscriptions',
                data: defaultDataSubs,
                backgroundColor: [
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(0,107,186,0.48)',
                    'rgba(155,135,12,0.59)',
                ],
                borderColor: [
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
                    'rgb(1,129,224)',
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