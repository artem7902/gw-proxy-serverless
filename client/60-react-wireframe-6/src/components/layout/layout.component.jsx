import React from "react";
import "./layout.styles.css";
import { Layout, Menu } from "antd";
import { MenuUnfoldOutlined, MenuFoldOutlined } from "@ant-design/icons";
import Wireframe6 from "../wireframe-6/wireframe-6.component";

const { Header, Sider } = Layout;

class LayoutComponent extends React.Component {
  state = {
    collapsed: false
  };

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed
    });
  };

  render() {
    return (
      <Layout>
        <Sider
          trigger={null}
          className="site-layout-height"
          collapsible
          // collapsed={this.state.collapsed}
        >
          <div className="logo">
            <strong>GLASSWALL</strong>
          </div>
          <Menu theme="dark" mode="inline" defaultSelectedKeys={["1"]}>
            <Menu.Item key="1">
              <span>Wireframe 6</span>
            </Menu.Item>
          </Menu>
        </Sider>
        <Layout className="site-layout">
          <Header className="site-layout-background" style={{ padding: 0 }}>
            {React.createElement(
              this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined,
              {
                className: "trigger",
                onClick: this.toggle
              }
            )}
          </Header>

          <Wireframe6 />
        </Layout>
      </Layout>
    );
  }
}

export default LayoutComponent;
