import React from 'react';
import BaseLayout from './BaseLayout';

const NewTab = () => {
  return (
    <BaseLayout>
      <div>
        Today is a Study Day!!!
      </div>
      <div>
        <span>Morning</span>
        <span>Afternoon</span>
        <span>Evening</span>
      </div>
    </BaseLayout>
  );
};

export default NewTab;