import React from 'react';
import ReactSpeedometer      from 'react-d3-speedometer';

/**
 * A stardard component which show how mature decision is
 * @returns {ReactSpeedometer} a component
 * @constructor
 */
export default function DecisionGauge({value = 500, height = 120, scale = 64}) {
  return <ReactSpeedometer
    maxSegmentLabels={0}
    segments={scale}
    needleHeightRatio={0.7}
    value={value}
    height={height}
    width={height * 2}
    ringWidth={35}
  />

}