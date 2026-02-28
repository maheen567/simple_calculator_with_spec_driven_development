/**
 * Creating a sidebar enables you to link between the different docs.
 * You can find more here: https://docusaurus.io/docs/docs/sidebar#custom-sidebar
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}*/
const sidebars = {
  // But you can create any used sidebar on your own.
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        '1-robotic-nervous-system/chapter-1-foundations-of-ros2',
        '1-robotic-nervous-system/chapter-2-ai-to-controller-integration',
        '1-robotic-nervous-system/chapter-3-urdf-for-humanoids',
      ],
    },
  ],
};

module.exports = sidebars;
