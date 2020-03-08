
import React, { Fragment } from 'react'
import Highcharts from 'highcharts';


class LineChart extends React.Component {



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
                type: 'line',
                renderTo: 'chart-container' + this.props.id
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
                }


            },

            xAxis: {
                categories: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
            },

            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle'
            },

            plotOptions: {
                series: {
                    label: {
                        connectorAllowed: false
                    }
                }
            },

            series: this.props.data.data,

            responsive: {
                rules: [{
                    condition: {
                        maxWidth: 500
                    },
                    chartOptions: {
                        legend: {
                            layout: 'horizontal',
                            align: 'center',
                            verticalAlign: 'bottom'
                        }
                    }
                }]
            }
        });
    }

    render() {
        const {
            classes
        } = this.props;
        return (
            <Fragment>
                {typeof this.props.id !== "undefined" && <div id={"chart-container" + this.props.id}>
                </div>}
            </Fragment>

        );

    }

}
export default LineChart;