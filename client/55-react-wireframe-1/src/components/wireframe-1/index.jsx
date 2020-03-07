import React from "react";
import ReactSpeedometer from "react-d3-speedometer";
import { Table, Layout, Row, Col, Card } from "antd";
import { tm_data, yd_data, bhdata } from "./data";
import StackChart from "./StackChart";

// table columns
const tm_columns = [
  {
    title: "",
    dataIndex: "key",
    key: "key"
  },
  {
    title: "£, 000s ",
    dataIndex: "tm_price",
    key: "tm_price"
  },
  {
    title: "vs Budget",
    dataIndex: "tm_vsb",
    key: "tm_vsb"
  },
  {
    title: "vs Prev Year",
    dataIndex: "tm_vpy",
    key: "tm_vpy"
  }
];
const yd_columns = [
  {
    title: "£, 000s ",
    dataIndex: "yd_price",
    key: "yd_price"
  },
  {
    title: "vs Budget",
    dataIndex: "yd_vsb",
    key: "yd_vsb"
  },
  {
    title: "vs Prev Year",
    dataIndex: "yd_vpy",
    key: "yd_vpy"
  }
];

const { Content } = Layout;
const Wireframe1 = () => {
  return (
    <React.Fragment>
      <h1 className="pl-4 pt-4">Overview</h1>
      <Content className="content">
        <Row gutter={[16, 16]}>
          <Col md={12} sm={24}>
            {/* <div style={{ display: "flex", justifyContent: "flex-end" }}>
              <ReactSpeedometer
                value={500}
                needleColor="steelblue"
                needleTransitionDuration={4000}
                needleTransition="easeElastic"
                width={250}
                height={200}
                textColor={"transparent"}
              />
            </div> */}
            <h4>Progress: This Month</h4>
            <Table
              columns={tm_columns}
              dataSource={tm_data}
              pagination={false}
              bordered={true}
            />
          </Col>
          <Col md={12} sm={24}>
            <h4> Year to Date</h4>
            <Table
              columns={yd_columns}
              dataSource={yd_data}
              pagination={false}
              bordered={true}
            />
          </Col>
        </Row>
      </Content>
      <Content className="content">
        <Row gutter={[16, 16]}>
          <Col md={12} sm={24}>
            <h4>Revenue, Sow, Pipeline vs Fy TGT</h4>
            <div className="pb-5" style={{ width: "80%" }}>
              <StackChart />
            </div>
            <Card className="m-5" bordered={true} title="Key successes This Month">
              <ul>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
              </ul>
            </Card>
          </Col>
          <Col md={12} sm={24}>
            <h4>Business Health</h4>
            {bhdata.map(bh => (
              <Row>
                <Col>
                  <ReactSpeedometer
                    key={bh.title}
                    value={bh.value}
                    needleColor="steelblue"
                    needleTransitionDuration={4000}
                    needleTransition="easeElastic"
                    width={250}
                    height={150}
                    textColor={"transparent"}
                  />
                </Col>
                <Col className="pt-4">
                  <h5 className="text-underline">{bh.title}</h5>
                  <h5 className="text-pink">{bh.desc}</h5>
                </Col>
              </Row>
            ))}
          </Col>
        </Row>
      </Content>
    </React.Fragment>
  );
};

export default Wireframe1;
