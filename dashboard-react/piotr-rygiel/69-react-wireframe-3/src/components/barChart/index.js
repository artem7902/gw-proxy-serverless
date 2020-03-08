import React from 'react';
import {
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  BarChart,
  Bar,
  ResponsiveContainer,
  LabelList,
} from 'recharts';

const data = [
  {
    name: ' 1',
    TqT: 3800,
    Revenue: 34,
    Pipeline: 200,
    SOW: 1900,
    'YTD REV': 330,
  },
  {
    name: ' 2',
    TqT: 4300,
    Revenue: 23,
    Pipeline: 1300,
    SOW: 1100,
    'YTD REV': 500,
  },
  {
    name: ' 3',
    TqT: 4800,
    Revenue: 36,
    Pipeline: 1300,
    SOW: 1600,
    'YTD REV': 600,
  },
  {
    name: ' 4',
    TqT: 3800,
    Revenue: 73,
    Pipeline: 200,
    SOW: 1900,
    'YTD REV': 330,
  },
  {
    name: ' 5',
    TqT: 4300,
    Revenue: 21,
    Pipeline: 1300,
    SOW: 1100,
    'YTD REV': 500,
  },
  {
    name: ' 6',
    TqT: 4800,
    Revenue: 63,
    Pipeline: 1300,
    SOW: 1600,
    'YTD REV': 600,
  },
  {
    name: ' 7',
    TqT: 3800,
    Revenue: 25,
    Pipeline: 200,
    SOW: 1900,
    'YTD REV': 330,
  },
  {
    name: ' 8',
    TqT: 4300,
    Revenue: 12,
    Pipeline: 1300,
    SOW: 1100,
    'YTD REV': 500,
  },
  {
    name: ' 9',
    TqT: 4300,
    Revenue: 27,
    Pipeline: 700,
    SOW: 1400,
    'YTD REV': 700,
  },
  {
    name: ' 10',
    TqT: 5800,
    Revenue: 79,
    Pipeline: 1100,
    SOW: 1900,
    'YTD REV': 1500,
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
const getPath = (x, y, width, height) => {
  return `M ${x},${y} h ${width} v ${height} h ${-width} Z`;
};

const legendData = [
  {
    color: '#82ca9d',
    title: 'YTD REV',
  },
  {
    color: 'rgb(246, 150, 30)',
    title: 'SOW',
  },
  {
    color: '#8884d8',
    title: 'Pipeline',
  },
  {
    color: '#898989',
    title: 'TqT',
  },
];
const renderLegend = props => {
  return (
    <div
      style={{
        textAlign: 'left',
        marginLeft: 10,
        marginTop: -10,
        lineHeight: '20px',
      }}
    >
      {legendData.map(legend => {
        return (
          <div style={{ color: legend.color, fontWeight: 'bold' }}>
            {legend.title}
          </div>
        );
      })}
    </div>
  );
};
export default function _BarChart() {
  const maxY = 10000,
    CHART_HEIGHT = 400;
  const CustomBar = props => {
    const { fill, x, y, width, height, ex } = props;
    return (
      <g>
        <path d={getPath(x, y, width, height)} fill={fill}></path>
        <path
          d={getPath(x, (1 - props[ex] / maxY) * CHART_HEIGHT, width, 4)}
          fill="#898989"
        ></path>
        <g transform={`translate(${x + 10}, 20)`}>
          <text dy={16} textAnchor="middle" fill="#111">
            {`${props['Revenue']}%`}
          </text>
        </g>
      </g>
    );
  };
  return (
    <ResponsiveContainer width={'100%'} height={CHART_HEIGHT}>
      <BarChart data={data}>
        <CartesianGrid
          strokeDasharray="3 3"
          horizontal
          vertical
          verticalFill={['#f2f2f2', '#fff']}
          fillOpacity={0.2}
        />

        <XAxis
          dataKey="name"
          tick={CustomizedAxisTick}
          tickCount={data.length}
        />
        <YAxis domain={[0, maxY]} />
        <Tooltip />

        <Legend
          layout="vertical"
          align="right"
          verticalAlign="middle"
          content={renderLegend}
        />

        <Bar dataKey="YTD REV" barSize={20} stackId="a" fill="#82ca9d"></Bar>
        <Bar dataKey="SOW" barSize={20} stackId="a" fill="rgb(246, 150, 30)" />
        <Bar
          dataKey="Pipeline"
          barSize={20}
          stackId="a"
          fill="#8884d8"
          shape={<CustomBar fill="#0b5288" ex={'TqT'} />}
        >
          <LabelList dataKey="Gap" position="top"></LabelList>
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}
