import React from 'react';
import {
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  BarChart,
  Bar,
  ReferenceLine,
  ResponsiveContainer,
  LabelList,
} from 'recharts';

const data = [
  {
    name: '',
    Gap: 'Gap',
    Pipeline: 1300,
    'Stock of Work': 1600,
    Revenue: 400,
  },
];

export default function _BarChart() {
  return (
    <ResponsiveContainer width={'100%'} height={400}>
      <BarChart
        data={data}
        margin={{
          top: 20,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <XAxis dataKey="name" tick={null} />
        <YAxis domain={[0, 4500]} />
        <Tooltip />
        <Bar dataKey="Revenue" stackId="a" fill="#82ca9d" />
        <Bar dataKey="Stock of Work" stackId="a" fill="rgb(246, 150, 30)" />
        <Bar dataKey="Pipeline" stackId="a" fill="#8884d8">
          <LabelList dataKey="Gap" position="top"></LabelList>
        </Bar>
        <ReferenceLine
          y={4000}
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
        <Legend layout="vertical" align="right" verticalAlign="middle" />
      </BarChart>
    </ResponsiveContainer>
  );
}
