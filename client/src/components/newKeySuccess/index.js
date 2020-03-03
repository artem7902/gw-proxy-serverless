import React from 'react';
import { Card, Icon } from 'semantic-ui-react';

const description = ['Key Risks + Successful Planning'].join(' ');

const NewKeySuccess = () => (
  <Card fluid>
    <Card.Content header="Key Success, Warranties, Capacity Issues" />
    <Card.Content description={description} />
    <div style={{ height: 160 }}></div>
  </Card>
);

export default NewKeySuccess;
