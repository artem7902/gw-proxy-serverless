import React, { Component } from "react";
import CanvasJSReact from "../../assets/canvas/canvasjs.react";

var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class StackChart extends Component {
  constructor() {
    super();
    this.toggleDataSeries = this.toggleDataSeries.bind(this);
  }
  toggleDataSeries(e) {
    if (typeof e.dataSeries.visible === "undefined" || e.dataSeries.visible) {
      e.dataSeries.visible = false;
    } else {
      e.dataSeries.visible = true;
    }
    this.chart.render();
  }
  render() {
    const options = {
      animationEnabled: true,
      axisY: {
        title: "£, m",
        gridDashType: "dot",
        stripLines:[
          {                
            startValue:28,
            endValue:28.1,                
            color:"#00000",
            label: "Target",
            labelAlign: "far",
          }
        ]
      },
      toolTip: {
        shared: true,
        reversed: true
      },
      legend: {
        verticalAlign: "center",
        horizontalAlign: "right",
        reversed: true,
        cursor: "pointer",
        itemclick: this.toggleDataSeries
      },
      data: [
        {
          type: "stackedColumn",
          name: "Pipeline",
          showInLegend: true,
          yValueFormatString: "#,###m",
          dataPoints: [
            { label: " ", y: 10 }
          ]
        },
        {
          type: "stackedColumn",
          name: "Stock work",
          showInLegend: true,
          yValueFormatString: "#,###m",
          dataPoints: [
            { label: " ", y: 8 }
          ]
        },
        {
          type: "stackedColumn",
          name: "Revenue",
          showInLegend: true,
          yValueFormatString: "#,###m",
          dataPoints: [
            { label: " ", y: 7 }
          ]
        }
      ]
    };
    return (
      <div>
        <CanvasJSChart options={options} onRef={ref => (this.chart = ref)} />
      </div>
    );
  }
}

export default StackChart;
