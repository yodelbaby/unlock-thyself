
import React, { useMemo, forwardRef } from 'react';

interface RorschachImageProps {
  width?: number;
  height?: number;
  points?: number;
  complexity?: number;
}

const RorschachImage = forwardRef<SVGSVGElement, RorschachImageProps>(({
  width = 500,
  height = 350,
  points = 8,
  complexity = 0.75,
}, ref) => {
  const pathData = useMemo(() => {
    const halfWidth = width / 2;
    let path = `M ${halfWidth},${height} `; // Start at bottom center

    const randomPoints = Array.from({ length: points }, (_, i) => {
      const x = halfWidth + (Math.random() - 0.5) * halfWidth * complexity;
      const y = (height / points) * i + (Math.random() - 0.5) * 50;
      return { x: Math.max(halfWidth * (1-complexity), Math.min(width, x)), y: Math.max(0, Math.min(height, y)) };
    });
    
    randomPoints.sort((a,b) => b.y - a.y); // Sort points from top to bottom
    
    path += `L ${halfWidth},${randomPoints[0].y} `; // Line to top-ish center
    
    let lastPoint = { x: halfWidth, y: randomPoints[0].y };

    for (const point of randomPoints) {
      const cp1x = lastPoint.x + (Math.random() - 0.5) * 100;
      const cp1y = lastPoint.y + (Math.random() - 0.5) * 100;
      const cp2x = point.x - (Math.random() - 0.5) * 100;
      const cp2y = point.y - (Math.random() - 0.5) * 100;
      path += `C ${cp1x},${cp1y} ${cp2x},${cp2y} ${point.x},${point.y} `;
      lastPoint = point;
    }
    
    path += `L ${halfWidth},0 L ${halfWidth},${height} Z`; // Close path along the center line

    return path;
  }, [width, height, points, complexity]);

  return (
    <svg ref={ref} width="100%" height="100%" viewBox={`0 0 ${width} ${height}`} className="bg-white">
      <defs>
        <path id="rorschach-half" d={pathData} />
      </defs>
      
      <use href="#rorschach-half" fill="black" />
      <use href="#rorschach-half" fill="black" transform={`scale(-1 1) translate(-${width} 0)`} />
    </svg>
  );
});

export default RorschachImage;
