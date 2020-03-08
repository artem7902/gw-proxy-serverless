import React, { useState } from 'react';
import './style.scss';
export default function RoadMap() {
  const months = ['Month1', 'Month2', 'Month3', 'Month4', 'Month5', 'Month6'];
  const [current, setCurrent] = useState(0);
  return (
    <ul className="nav nav-tabs wizard">
      {months.map((month, index) => {
        return (
          <li
            key={month}
            className={
              index == current ? 'active' : index < current ? 'completed' : ''
            }
            onClick={() => setCurrent(index)}
          >
            <a data-toggle="tab" aria-expanded="false">
              {month}
            </a>
          </li>
        );
      })}
    </ul>
  );
}
