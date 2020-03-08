import React from 'react';
import {
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  BarChart,
  Bar,
  ReferenceLine,
  ResponsiveContainer,
} from 'recharts';

const data = [
  {
    name: 'J',
    ACTVAL: 1300,
  },
  {
    name: 'F',
    ACTVAL: 2800,
  },
  {
    name: 'M',
    BUDGET: 1600,
    FY19: 1800,
  },
  {
    name: 'A',
    BUDGET: 1700,
    FY19: 1800,
  },
  {
    name: 'M',
    BUDGET: 1790,
    FY19: 1700,
  },
  {
    name: 'J',
    BUDGET: 1800,
    FY19: 1700,
  },
  {
    name: 'J',
    BUDGET: 2000,
    FY19: 1800,
  },
  {
    name: 'A',
    BUDGET: 2100,
    FY19: 1870,
  },
  {
    name: 'S',
    BUDGET: 2130,
    FY19: 1980,
  },
  {
    name: 'O',
    BUDGET: 2200,
    FY19: 2030,
  },
  {
    name: 'N',
    BUDGET: 2300,
    FY19: 2090,
  },
  {
    name: 'D',
    BUDGET: 2700,
    FY19: 2400,
  },
];
const CustomizedAxisTick = props => {
  const { x, y, payload } = props;

  return (
    <g transform={`translate(${x},${y})`}>
      <text dy={16} textAnchor="middle" fill="#666">
        {payload.value}
      </text>
    </g>
  );
};
export default function _BarChart() {
  return (
    <ResponsiveContainer width={'100%'} height={300}>
      <BarChart
        data={data}
        margin={{
          top: 20,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis
          dataKey="name"
          allowDecimals={false}
          tick={<CustomizedAxisTick />}
        />
        <YAxis />
        <Tooltip />
        <Bar dataKey="BUDGET" stackId="a" fill="rgb(246, 150, 30)" />
        <Bar dataKey="FY19" stackId="a" fill="#8884d8" />
        <Bar dataKey="ACTVAL" stackId="a" fill="#82ca9d" />
        <ReferenceLine
          y={3000}
          label={{
            position: 'right',
            value: 'Tqt',
            fill: 'red',
            fontSize: 14,
            textAlign: 'right',
          }}
          stroke="red"
          strokeDasharray="3 3"
        />
      </BarChart>
    </ResponsiveContainer>
  );
}
