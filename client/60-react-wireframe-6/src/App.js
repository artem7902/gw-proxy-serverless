import React from "react";
import "./App.css";

import ReactSpeedometer from "react-d3-speedometer";
import { Table } from "antd";
import {
  ArrowUpOutlined,
  ArrowDownOutlined,
  LineOutlined
} from "@ant-design/icons";

// table dummy data
const data = [
  {
    key: "1",
    keyMatrics: "AVERAGE DEX SIZE",
    thisMonth: 32,
    lastMonth: 32
  },
  {
    key: "2",
    keyMatrics: "AVERAGE DAYS TO PAYMENT",
    thisMonth: 32,
    lastMonth: 60
  },
  {
    key: "3",
    keyMatrics: "AVERAGE WIP",
    thisMonth: 43,
    lastMonth: 32
  },
  {
    key: "4",
    keyMatrics: "AVERAGE DEST.",
    thisMonth: 29,
    lastMonth: 20
  }
];

// table columns
const columns = [
  {
    title: "KEY MATRICS",
    dataIndex: "keyMatrics",
    key: "keyMatrics",
    render: text => <div>{text}</div>
  },
  {
    title: "THIS MONTH",
    dataIndex: "thisMonth",
    key: "thisMonth"
  },
  {
    title: "LAST MONTH",
    dataIndex: "lastMonth",
    key: "lastMonth"
  },
  {
    title: "TREND",
    key: "trends",
    dataIndex: "trends",
    render: (text, row) => (
      <span>
        {row.thisMonth === row.lastMonth && (
          <LineOutlined style={{ color: "grey" }} />
        )}
        {row.thisMonth < row.lastMonth && (
          <ArrowDownOutlined style={{ color: "red" }} />
        )}
        {row.thisMonth > row.lastMonth && (
          <ArrowUpOutlined style={{ color: "green" }} />
        )}
      </span>
    )
  }
];

function App() {
  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-12 col-md-5">
          <h6 className="App-text-underline">FINANCES</h6>
          <h6 className="App-text-underline">HEADLINES</h6>
          <div></div>
        </div>
        <div className="col-12 col-md-7">
          <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <ReactSpeedometer
              value={500}
              needleColor="steelblue"
              needleTransitionDuration={4000}
              needleTransition="easeElastic"
              width={200}
              height={200}
            />
          </div>
          <Table
            columns={columns}
            dataSource={data}
            footer={() => <span style={{ color: "green" }}>KEY SUCCESSES</span>}
          />
        </div>
      </div>
      <div className="row p-2">
        <h6 className="App-text-underline">FINANCIAL SUMMARY</h6>
        <div
          style={{ height: "300px", width: "100%", border: "1px solid black" }}
        ></div>
      </div>
    </div>
  );
}

export default App;
