import React from 'react';
import './style.scss';
export default function DecisionRequired({ title = "Decision Required", notes = ['', '', '',] }) {

  return (
    <div className="note">
      <div className="note-header">{title}</div>
      <div className="note-content">
        {notes.map((item, index) => {
          return (
            <div className="note-item" key={index}>
              <div className="note-index">{index + 1}</div>
              <div className="note-item-content">{item}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
