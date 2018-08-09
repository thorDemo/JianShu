/* 二维图表 */
let myChart = echarts.init(document.getElementById('chart-panel'));

window.onload = function () {
    myChart.setOption({
        title: {
            text: '蜘蛛数量统计',
            subtext: '按时间分布'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['百度蜘蛛', '神马蜘蛛', '360蜘蛛', '搜狗蜘蛛']
        },
        toolbox: {
            show: true,
            feature: {
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        xAxis: [
            {
                type: 'category',
                data: []
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '百度蜘蛛',
                type: 'bar',
                data: [],
                markPoint: {
                    data: [
                        {type: 'max', name: '最大值'},
                        {type: 'min', name: '最小值'}
                    ]
                },
                markLine: {
                    data: [
                        {type: 'average', name: '平均值'}
                    ]
                }
            },
            {
                name: '神马蜘蛛',
                type: 'bar',
                data: [],
                markPoint: {
                    data: [
                        {type: 'max', name: '最大值'},
                        {type: 'min', name: '最小值'}
                    ]
                },
                markLine: {
                    data: [
                        {type: 'average', name: '平均值'}
                    ]
                }
            },
            {
                name: '360蜘蛛',
                type: 'bar',
                data: [],
                markPoint: {
                    data: [
                        {type: 'max', name: '最大值'},
                        {type: 'min', name: '最小值'}
                    ]
                },
                markLine: {
                    data: [
                        {type: 'average', name: '平均值'}
                    ]
                }
            },
            {
                name: '搜狗蜘蛛',
                type: 'bar',
                data: [],
                markPoint: {
                    data: [
                        {type: 'max', name: '最大值'},
                        {type: 'min', name: '最小值'}
                    ]
                },
                markLine: {
                    data: [
                        {type: 'average', name: '平均值'}
                    ]
                }
            }
        ]
    })
};

$.getJSON('/spider_data/day/', function (data) {
    myChart.hideLoading();
    myChart.setOption({
        title:{
            subtext: '最近7天的数据'
        },
        xAxis:[{
            data: data['category']
        }],
        series: [
            {
                name: '百度蜘蛛',
                data: data['Baidu'],
            }, {
                name: '神马蜘蛛',
                data: data['Yisou'],
            }, {
                name: '360蜘蛛',
                data: data['Yisou'],
            }, {
                name: '搜狗蜘蛛',
                data: data['Yisou'],
            },
        ],
    });
});

function day() {
    myChart.showLoading();
    $.getJSON('/spider_data/day/', function (data) {
        myChart.hideLoading();
        myChart.setOption({
            title: {
                subtext: '最近7天的数据'
            },
            xAxis: [{
                data: data['category']
            }],
            series: [
                {
                    name: '百度蜘蛛',
                    data: data['Baidu'],
                }, {
                    name: '神马蜘蛛',
                    data: data['Yisou'],
                }, {
                    name: '360蜘蛛',
                    data: data['Yisou'],
                }, {
                    name: '搜狗蜘蛛',
                    data: data['Yisou'],
                },
            ],
        });
    });
}

function hours() {
    myChart.showLoading();
    $.getJSON('/spider_data/hou/', function (data) {
        myChart.hideLoading();
        myChart.setOption({
            title: {
                subtext: '最近7天的数据'
            },
            xAxis: [{
                data: data['category']
            }],
            series: [
                {
                    name: '百度蜘蛛',
                    data: data['Baidu'],
                }, {
                    name: '神马蜘蛛',
                    data: data['Yisou'],
                }, {
                    name: '360蜘蛛',
                    data: data['Yisou'],
                }, {
                    name: '搜狗蜘蛛',
                    data: data['Yisou'],
                },
            ],
        });
    });
}

