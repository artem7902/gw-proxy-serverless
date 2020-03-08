import React from 'react';
import './style.scss';
export default function Product({ name }) {
  return (
    <div className="product-line">
      <div className="product-line-name">{name}</div>
      <div className="product-line-desc"></div>
    </div>
  );
}
