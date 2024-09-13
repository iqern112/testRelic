function createChart(context, labels, data) {
    new Chart(context, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Response Time (ms)',
                data: data,
                borderColor: 'rgb(75, 192, 192)',
                fill: false,
                tension: 0.1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'second'
                    }
                },
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
