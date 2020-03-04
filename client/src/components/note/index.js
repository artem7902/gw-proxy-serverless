import React from 'react';
import './style.scss';
const alpha = [
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
  'G',
  'H',
  'I',
  'J',
  'K',
  'L',
  'M',
  'N',
  'O',
  'P',
  'Q',
  'R',
  'S',
  'T',
  'U',
  'V',
  'W',
  'X',
  'Y',
  'Z',
];
const data = ['', '', '', '', ''];
export default function Note({ title, asc }) {
  return (
    <div className="note">
      <div className="note-header">{title}</div>
      <div className="note-content">
        {data.map((item, index) => {
          return (
            <div className="note-item" key={index}>
              <div className="note-index">{asc ? alpha[index] : index + 1}</div>
              <div className="note-item-content">{item}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
