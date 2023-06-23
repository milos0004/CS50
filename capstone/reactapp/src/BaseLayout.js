import React from 'react';
import './App.css';

const BaseLayout = ({ children }) => {
  return (
    <div>
      {/* Common header */}
      <header className='App-header'>
        Welcome, Milos!
      </header>

      {/* Page content */}
      <main>
        {children}
      </main>

      {/* Common footer */}
      <footer>
        Settings
      </footer>
    </div>
  );
};

export default BaseLayout;