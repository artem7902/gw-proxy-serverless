import React from 'react'
import CanvasJSReact from '../../assets/canvasjs.react';




var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class StackedColumnChart extends React.Component{
    constructor() {
		super();
		this.toggleDataSeries = this.toggleDataSeries.bind(this);
	}
	toggleDataSeries(e){
		if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
			e.dataSeries.visible = false;
		}
		else{
			e.dataSeries.visible = true;
		}
		this.chart.render();
	}
	render() {
		const options = {
			animationEnabled: true,
			exportEnabled: false,
			dataPointWidth: 140,
			
			axisY: {
				gridThickness: 0,
				title: "£, m",
				prefix: " ",
				suffix: " ",
				stripLines:[
					{                
						value:28,
						color:"black",
						thickness:4,
						label : "TGT",
						labelFontColor:"black",
						labelFontSize:16,
						lineDashType: "dot",                
					}
				]
			},
			toolTip: {
				shared: false,
				reversed: false
			},
			legend: {
				verticalAlign: "center",
				horizontalAlign: "right",
				reversed: false,
				cursor: "pointer",
				itemclick: this.toggleDataSeries,
				fontSize: 20
			},
			data: [
			{
				type: "stackedColumn",
				name: "Revenue",
				showInLegend: true,
				yValueFormatString: "#,###k",
				dataPoints: [
					{ label: "", y: 7 }
				]
			},
			{
				type: "stackedColumn",
				name: "Stock of work",
				showInLegend: true,
				yValueFormatString: "#,###k",
				dataPoints: [
					{ label: " ", y: 10 }
				]
			},
			{
				type: "stackedColumn",
				name: "Weighted Pipelining",
				showInLegend: true,
				yValueFormatString: "#,###k",
				dataPoints: [
					{ label: " ", y: 8 }
			]
			}]
		}
		
		return (
		<div>			
			<CanvasJSChart options = {options} 
				onRef={ref => this.chart = ref}
			/>			
		</div>
		);
	}
}
export default StackedColumnChart