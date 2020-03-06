import React from 'react'
import {
  ResponsiveContainer,
  ScatterChart,
  Tooltip,
  Legend,
  Label,
  Scatter,
  CartesianGrid,
  XAxis,
  YAxis,
  ZAxis,
} from 'recharts';

const data01 = [
  {
    "x": 1,
    "y": 100,
    "z": 10
  },
  {
    "x": 2,
    "y": 200,
    "z": 20
  },
  {
    "x": 3,
    "y": 300,
    "z": 30
  },
];
const data02 = [
  {
    "x": 1,
    "y": 400,
    "z": 40
  },
  {
    "x": 2,
    "y": 500,
    "z": 50
  },
  {
    "x": 3,
    "y": 600,
    "z": 60
  }
];


export default function MarketProductsChart() {

  return (
    <ScatterChart width={500} height={400}
                  margin={{top: 20, right: 20, bottom: 20}}
    >
      <CartesianGrid horizontal={true} vertical/>
      <XAxis dataKey="x" name="product" type='number'>
        <Label value="Product / Services" offset={100}/>
      </XAxis>
      <YAxis dataKey="y" name="market" label={{value: 'Markets', angle: -90, position: 'insideLeft'}}>
        {/*<Label value="Markets" angle={-90}/>*/}
      </YAxis>
      <ZAxis dataKey="z" range={[0, 1000]} name="score"/>
      <Tooltip cursor={{strokeDasharray: '3 3'}}/>
      <Legend/>
      <Scatter name="Current" data={data01} fill="#297A67"/>
      <Scatter name="End FY TAT" data={data02} fill="#F86642"/>
    </ScatterChart>
  )
}
