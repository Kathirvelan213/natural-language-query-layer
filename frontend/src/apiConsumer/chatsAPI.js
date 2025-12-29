function getChatList() {
  return [
    [1, "CSS Grid Layout Basics"],
    [2, "JavaScript Event Bubbling"],
    [3, "Responsive Navbar Design"],
    [4, "API Rate Limiting Explained"],
    [5, "Dark Mode Implementation"],
    [6, "Flexbox vs Grid Comparison"],
    [7, "Building a To-Do App"],
    [8, "Web Accessibility Basics"],
    [9, "Authentication with JWT"],
    [10, "Optimizing Website Performance"],
    [11, "Understanding Async/Await"],
    [12, "Image Optimization Techniques"],
    [13, "State Management in React"],
    [14, "Form Validation Strategies"],
    [15, "Deploying a Web App"],
    [16, "SEO Best Practices"],
  ];
}

function getChatConversation(id) {
  const chats= {
    1: [
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
    ],
    2: [
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
    ],
    3: [
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
    ],
    4: [
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
    ],
    5: [
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
    ],
    6: [
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
      ["qn", "sql", "response"],
    ],
  };
  return chats[id];
}

export { getChatList, getChatConversation };
