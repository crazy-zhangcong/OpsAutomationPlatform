/**
 * Created by wupeiqi on 17/2/24.
 * 用于资产首页基本图标的展示
 */
function initBusiness() {
    var options = {
        credits: {
            text: 'oldboyedu',
            href: 'http://www.oldboyedu.com'
        },
        chart: {
            type: 'column',
            options3d: {
                enabled: true,
                alpha: 10,
                beta: 25,
                depth: 70
            }
        },
        title: {
            text: '3D chart with null values'
        },
        subtitle: {
            text: 'Notice the difference between a 0 value and a null point'
        },
        plotOptions: {
            column: {
                depth: 25
            }
        },
        xAxis: {
            //categories: Highcharts.getOptions().lang.shortMonths
            categories: ['业务线A', '业务线B', '业务线C']
        },
        yAxis: {
            allowDecimals: true,
            title: {
                text: '资产数量'
            }
        },
        series: [{
            name: '服务器',
            data: [2, 3, null]
        }, {
            name: '路由器',
            data: [2, 3, null]
        }, {
            name: '资产',
            data: [2, 3, null]
        }
        ]
    };
    $.ajax({
        url: '/chart-business.html',
        method: 'GET',
        dataType: 'JSON',
        success: function (arg) {
            if (arg.status) {
                options.xAxis.categories = arg.data.categories;
                options.series = arg.data.series;
                $('#container_business').highcharts(options);
            } else {
                alert(arg.message);
            }
        }
    });

}

function initCategory() {
    var options = {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Browser market shares January, 2015 to May, 2015'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: [{
                name: 'IE',
                y: 56.33
            }, {
                name: 'Chrome',
                y: 24.03,
                sliced: true,
                selected: true
            }, {
                name: 'Firefox',
                y: 10.38
            }, {
                name: 'Safari',
                y: 4.77
            }, {
                name: 'Opera',
                y: 0.91
            }, {
                name: 'Propri',
                y: 0.2
            }]
        }]
    };
    $('#container_category').highcharts(options);
}

function initGroup() {
    var options = {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Historic World Population by Region'
        },
        subtitle: {
            text: 'Source: <a href="https://en.wikipedia.org/wiki/World_population">Wikipedia.org</a>'
        },
        xAxis: {
            categories: ['Africa', 'America', 'Asia', 'Europe', 'Oceania'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Population (millions)',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' millions'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 80,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Year 1800',
            data: [107, 31, 635, 203, 2]
        }, {
            name: 'Year 1900',
            data: [133, 156, 947, 408, 6]
        }, {
            name: 'Year 2012',
            data: [1052, 954, 4250, 740, 38]
        }]
    };
    $('#container_group').highcharts(options);
}

function initDynamic() {
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });
    (function () {
        var lastId = 0;
        Highcharts.stockChart('container_dynamic', {
            chart: {
                events: {
                    load: function () {
                        var series = this.series[0];
                        /*
                         function fetch_data(){
                         $.ajax({
                         url: '/chart-dynamic.html',
                         method: 'GET',
                         data: {'last_id': lastId},
                         dataType: 'JSON',
                         success: function (arg) {
                         $.each(arg.data, function (k, v) {
                         //series.addPoint([v.x, v.y],true,false);
                         series.addPoint([v.x, v.y],true,true);
                         });
                         lastId = arg.last_id;
                         console.log(arg);
                         fetch_data();
                         }
                         });
                         }
                         fetch_data();
                         */

                        setInterval(function () {
                            $.ajax({
                                url: '/chart-dynamic.html',
                                method: 'GET',
                                data: {'last_id': lastId},
                                dataType: 'JSON',
                                success: function (arg) {
                                    $.each(arg.data, function (k, v) {
                                        //series.addPoint([v.x, v.y], true, false);
                                        series.addPoint([v.x, v.y], true, true);
                                    });
                                    lastId = arg.last_id;
                                }
                            });
                        }, 3000);

                    }
                }
            },
            rangeSelector: {
                buttons: [{
                    count: 1,
                    type: 'minute',
                    text: '1M'
                }, {
                    count: 5,
                    type: 'minute',
                    text: '5M'
                }, {
                    type: 'all',
                    text: 'All'
                }],
                inputEnabled: false,
                selected: 0
            },

            title: {
                text: 'Live random data'
            },
            tooltip: {
                xDateFormat: "%Y-%m-%d %H:%M:%S",
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
                valueDecimals: 1
            },
            xAxis: {
                type: 'datetime',
                labels: {
                    step: 3,
                    formatter: function () {
                        return Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.value);
                    }
                }
            },
            series: [{
                name: 'Random data',
                data: (function () {
                    var data = [];
                    $.ajax({
                        url: '/chart-dynamic.html',
                        method: 'GET',
                        data: {'last_id': lastId},
                        async: false,
                        dataType: 'JSON',
                        success: function (arg) {
                            $.each(arg.data, function (k, v) {
                                data.push([v.x, v.y]);
                            });
                            lastId = arg.last_id;
                            return data;
                        }
                    });
                    return data

                }())
            }]
        });
    })();

}