
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
                text: "",
                align: 'left'
            },
            
            chart: {
                type: 'column',
                renderTo: 'container'
            },
            yAxis: {
                title: {
                    text: "£'000s",                    
                    style:{
                        fontWeight:"bold",
                        fontSize:"15px",
                        color: "#333333"   
                    }                                 
                },
                stackLabels: {
                    qTotals: ['____','____','____','____','____', '____', '____', '____', '____', '____'],
                    enabled: true,
                    style: {
                        fontWeight:"bold",
                        color: ( // theme
                            Highcharts.defaultOptions.title.style && Highcharts.defaultOptions.title.style.color
                        ) || '#333333'
                    },
                    formatter: function() {            
                        return this.options.qTotals[this.x];
                    }
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
                
            },

            xAxis: {
                categories: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],               
                title:{
                    text:"Client",
                    align: "left",
                    style:{                        
                        fontSize: "13px",
                        fontWeight:"bold",
                        color: "#333333"
                    },
                    y:-20
                },
                gridLineWidth: 1,
               
                plotLines: [{
                    color: '#FF0000',
                    width: 0,
                    value:0,
                    label:{
                        text: "% of co revenue" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 1,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 2,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 3,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 4,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 5,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 6,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 7,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },
                {
                    color: '#FF0000',
                    width: 0,
                    value: 8,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                },{
                    color: '#FF0000',
                    width: 0,
                    value: 9,
                    label:{
                        text: "%" ,
                        style:{
                            fontSize:"12px"
                        }                       
                    },
                }
            ]

            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle'
            },
            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                shared: false
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
                name: 'PIPELINE',
                color: "#c564c5",
                data: [2, 1, 3, 2, 4, 1, 3, 1, 3, 4]
            }, {
                name: 'SOW',
                color: "#f7b949",
                data: [2, 2, 1, 3, 3, 2, 4, 1, 2, 2]
            },{
                name: 'YTD REV',
                color: "#64a86b",
                data: [2, 2, 1, 1, 3, 2, 2, 2, 2,3]
            },
            {
                name: 'TGT',
                color: "#000000",
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            }
        ]

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
            </Fragment>

        );

    }

}
export default StackedChart;