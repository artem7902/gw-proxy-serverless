import React, { useState } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';

const ACTVAL_COLOR = '#449580';
const FORECAST_COLOR = '#343434';
const BUDGET_COLOR = '#f0916a';
const FY19_COLOR = '#f7a7e5';
const MARGIN_COLOR = '#723987';

const data = [
  {
    name: 'J',
    ACTVAL: 1300,
    BUDGET: 1400,
    FY19: 1600,
    MARGIN: 1200,
  },
  {
    name: 'F',
    ACTVAL: 1400,
    BUDGET: 1500,
    FY19: 1700,
    MARGIN: 1210,
  },
  {
    name: 'M',
    ACTVAL: 1440,
    BUDGET: 1600,
    FY19: 1800,
    MARGIN: 1290,
  },
  {
    name: 'A',
    ACTVAL: 1500,
    BUDGET: 1700,
    FY19: 1800,
    MARGIN: 1400,
  },
  {
    name: 'M',
    ACTVAL: 1700,
    BUDGET: 1790,
    FY19: 1700,
    MARGIN: 1500,
  },
  {
    name: 'J',
    ACTVAL: 1900,
    BUDGET: 1800,
    FY19: 1700,
    MARGIN: 1530,
  },
  {
    name: 'J',
    ACTVAL: 2200,
    FORECAST: 2200,
    BUDGET: 2000,
    FY19: 1800,
    MARGIN: 1600,
  },
  {
    name: 'A',
    FORECAST: 2300,
    BUDGET: 2100,
    FY19: 1870,
    MARGIN: 1700,
  },
  {
    name: 'S',
    FORECAST: 2400,
    BUDGET: 2130,
    FY19: 1980,
    MARGIN: 1800,
  },
  {
    name: 'O',
    FORECAST: 2500,
    BUDGET: 2200,
    FY19: 2030,
    MARGIN: 1900,
  },
  {
    name: 'N',
    FORECAST: 2600,
    BUDGET: 2300,
    FY19: 2090,
    MARGIN: 1920,
  },
  {
    name: 'D',
    FORECAST: 2800,
    BUDGET: 2700,
    FY19: 2400,
    MARGIN: 2100,
  },
];

export default function _LineChart({ revenue }) {
  const [opacity, setOpacity] = useState({
    act: 1,
    budget: 1,
    fy19: 1,
    margin: 1,
  });

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
        <div className="recharts-legend-item">
          <span style={{ color: ACTVAL_COLOR }}>ACTVAL</span>
          <span style={{ color: FORECAST_COLOR }}> + FORECAST</span>
        </div>
        <div className="recharts-legend-item" style={{ color: BUDGET_COLOR }}>
          BUDGET
        </div>
        <div className="recharts-legend-item" style={{ color: FY19_COLOR }}>
          FY19
        </div>
        {revenue ? (
          <div className="recharts-legend-item" style={{ color: MARGIN_COLOR }}>
            MARGIN
          </div>
        ) : null}
      </div>
    );
  };

  const handleMouseEnter = o => {
    console.log('legend over', o);
    // const { dataKey } = o;
    // const { opacity } = this.state;
    // setOpacity({ ...opacity, [dataKey]: 0.5 });
  };

  const handleMouseLeave = o => {
    // const { dataKey } = o;
    // const { opacity } = this.state;
    // setOpacity({ ...opacity, [dataKey]: 1 });
  };
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
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart
        data={data}
        margin={{
          top: 15,
          right: 20,
          left: 20,
          bottom: 15,
        }}
        isAnimationActiveBoolean={false}
      >
        <CartesianGrid strokeDasharray="3 3" />

        <XAxis
          dataKey="name"
          allowDecimals={false}
          tick={<CustomizedAxisTick />}
        />
        <YAxis />
        <Tooltip />

        <Line
          type="monotone"
          dataKey="FORECAST"
          stroke={FORECAST_COLOR}
          dot={false}
          strokeDasharray="5 5"
          strokeWidth={3}
          strokeOpacity={opacity.act}
        />
        <Line
          type="linear"
          dataKey="ACTVAL"
          stroke={ACTVAL_COLOR}
          dot={false}
          strokeWidth={3}
          strokeOpacity={opacity.act}
        />
        <Line
          type="linear"
          dataKey="BUDGET"
          stroke={BUDGET_COLOR}
          dot={false}
          strokeWidth={3}
          strokeOpacity={opacity.budget}
        />
        <Line
          type="linear"
          dataKey="FY19"
          stroke={FY19_COLOR}
          dot={false}
          strokeWidth={3}
          strokeOpacity={opacity.fy19}
        />
        {revenue ? (
          <Line
            type="linear"
            dataKey="MARGIN"
            stroke={MARGIN_COLOR}
            dot={false}
            strokeWidth={3}
            strokeOpacity={opacity.margin}
          />
        ) : null}

        <Legend
          layout="vertical"
          align="right"
          verticalAlign="top"
          onMouseEnter={() => handleMouseEnter()}
          onMouseLeave={() => handleMouseLeave()}
          content={renderLegend}
        />
      </LineChart>
    </ResponsiveContainer>
  );
}
