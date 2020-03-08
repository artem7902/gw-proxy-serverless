import React from 'react';
import ReactSpeedometer from 'react-d3-speedometer';
import './styles.scss';

const values = [
  {
    value: 500,
    title: 'SALES, REVENUE, SOW, PIPELINE',
  },
  {
    value: 400,
    title: 'KEY ACCOUNTS',
  },
  {
    value: 300,
    title: 'ENGINEERING',
  },
  {
    value: 600,
    title: 'FUTURE MARKETS + SALES',
  },
  {
    value: 700,
    title: 'FINANCIAL',
  },
];
export default function BusinessHealth() {
  return (
    <div className="business-health">
      {values.map(value => {
        return (
          <div className="business-health-feature">
            <div className="business-health-feature-speedometer">
              <ReactSpeedometer
                value={value.value}
                maxSegmentLabels={0}
                segments={1000}
                width={160}
                height={160}
                needleHeightRatio={0.7}
                currentValueText=""
                ringWidth={24}
              />
            </div>
            <div className="business-health-feature-title">{value.title}</div>
          </div>
        );
      })}
    </div>
  );
}
