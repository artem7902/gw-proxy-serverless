import 'bootstrap/dist/css/bootstrap.css';
import React from 'react';
import {
  Table,
  Image,
  Label
}            from 'semantic-ui-react';
import './style.scss';

const MarketProductsTable = ({
  data = [
    {images: [null, null, 'circle-1.png', 'circle.png']},
    {images: ['circle-5.png', 'circle-2.png', 'circle-4.png', 'circle.png']},
    {images: [null, 'circle-5.png', 'circle-3.png', 'circle-2.png']},
    {images: [null, null, 'circle-5.png', 'circle-6.png']},
  ]
}) => (
  <React.Fragment>
    <div className='d-flex flex-column'>
      <div>
        <Table celled style={{width: '400px'}}>
          <Table.Body>
            {data.map((row, yindex) => {
              return (
                <Table.Row key={`market-${yindex}`} style={{height: '100px'}}>
                  {data.map(({images = []}, xindex) => {
                    const imageSrc = images[yindex];

                    console.log(xindex, yindex, images, row, row.images, imageSrc);

                    const image = imageSrc ? <Image key={`img-${xindex}-${yindex}`} src={imageSrc} circular fluid/> : null;
                    return (
                      <Table.Cell width={1} key={`cell-${xindex}-${yindex}`}>
                        {image}
                      </Table.Cell>
                    );
                  })}
                </Table.Row>
              );
            })}
          </Table.Body>
        </Table>
        <div className='horizontal'>Products / Services</div>
        <div className='vertical'>Markets</div>
      </div>
    </div>
  </React.Fragment>
);

export default MarketProductsTable;
