import React from "react";
import ReactSpeedometer from "react-d3-speedometer";
import { Table, Layout, Row } from "antd";
import {
  ArrowUpOutlined,
  ArrowDownOutlined,
  LineOutlined
} from "@ant-design/icons";

import { data } from "./data";

const { Content } = Layout;
const Wireframe6 = () => {
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
  return (
    <div>
      <Row>
        <Content className="content">
          <div>
            <h6 className="text-underline">FINANCES</h6>
            <h6 className="text-underline">HEADLINES</h6>
          </div>
        </Content>
        <Content
          className="content"
          style={{ display: "flex", justifyContent: "flex-end" }}
        >
          <div>
            <div style={{ display: "flex", justifyContent: "flex-end" }}>
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
              footer={() => (
                <span style={{ color: "green" }}>KEY SUCCESSES</span>
              )}
            />
          </div>
        </Content>
      </Row>
      <Row>
        <Content className="content">
          <div className="row p-2">
            <h6 className="text-underline">FINANCIAL SUMMARY</h6>
            <div
              style={{
                height: "300px",
                width: "100%",
                border: "1px solid black"
              }}
            ></div>
          </div>
        </Content>
      </Row>
    </div>
  );
};

export default Wireframe6;
