import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'semantic-ui-css/semantic.min.css';

import ReactSpeedometer from 'react-d3-speedometer';
import { Row, Col, Container } from 'reactstrap';
import NewProductTable from './components/newProductTable';
import NewKeySuccess from './components/newKeySuccess';
import ProfitabilityTable from './components/profitabilityTable';
import RoadMap from './components/roadMap';
import Product from './components/product';
import KeySuccess from './components/keySuccess';
function App() {
  return (
    <div className="App">
      <Container>
        <Row className="mt-5">
          <div className="mt-1">
            <div className="title">Engineering</div>
            <div className="title">Roadmap</div>
          </div>
          <div className="ml-auto" style={{ height: 200 }}>
            <ReactSpeedometer value={500} />
          </div>
        </Row>
        <Row>
          <RoadMap />
        </Row>
        <div className="products">
          <Product name="Product 1" />
          <Product name="Product 2" />
          <Product name="Product 3" />
        </div>
        <div className="subtitle">New Product Development</div>
        <Row>
          <Col md={6}>
            <NewProductTable />
          </Col>
          <Col md={6}>
            <NewKeySuccess />
          </Col>
        </Row>
        <div className="subtitle">Profitability Per Product/Service</div>

        <Row>
          <Col md={6}>
            <ProfitabilityTable />
          </Col>
          <Col md={6}>
            <KeySuccess />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
