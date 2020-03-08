
import React, { Fragment } from 'react'
import Highcharts from 'highcharts';


class StackedChart extends React.Component {



    componentDidMount() {

        this.highChartsRender()

    }

    componentWillUnmount() {
    }



    highChartsRender() {

        Highcharts.chart({
            credits: { enabled: false },

            title: {
                text: this.props.data.title,
                align: 'left'
            },
            chart: {
                type: 'column',
                renderTo: 'container'
            },
            yAxis: {
                title: {
                    text: null
                },
                gridLineWidth: 0,
                minorGridLineWidth: 0,
                lineWidth: 1,
                labels: {
                    formatter: function () {
                        return '';
                    },
                    style: {
                        color: '#4572A7'
                    }
                },
                plotLines: [{
                    color: '#FF0000',
                    width: 2,
                    value: 9,
                    label: { text: "TGT", align: 'right',
                    y: -10, /*moves label down*/
                    x:20 }
                }]


            },

            xAxis: {
                categories: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle'
            },
            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                shared: true
            },
            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels: {
                        enabled: false
                    }
                }
            },
            series: [{
                name: 'Actual',
                color: "green",
                data: [4, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },{
                name: 'Margin',
                color: "purple",
                data: [0, 0, 5, 3, 2, 2, 2, 2, 3, 2, 2, 2]
            }, {
                name: 'Budget',
                color: "orange",
                data: [0, 0, 5, 3, 2, 5, 1, 3, 1, 3, 1, 5 ]
            }]

        });
    }

    render() {
        const {
            classes
        } = this.props;
        return (
            <Fragment>
                {<div id={"container"}>
                </div>}
            </Fragment >

        );

    }

}
export default StackedChart;